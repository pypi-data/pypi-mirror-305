# Copyright © 2011-2019 Red Hat, Inc. and others.
# This file is part of Bodhi.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""Bodhi's database models."""

from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from functools import lru_cache, partial
from textwrap import wrap
from urllib.parse import urljoin
import hashlib
import json
import re
import time
import typing
import uuid
import warnings

from mediawiki import MediaWiki
from packaging.version import parse as parse_version
from sqlalchemy import __version__ as sqlalchemy_version
from sqlalchemy import (
    and_,
    Boolean,
    Column,
    Date,
    DateTime,
    event,
    ForeignKey,
    func,
    Integer,
    or_,
    Table,
    Unicode,
    UnicodeText,
    UniqueConstraint,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import class_mapper, declarative_base, relationship, validates
from sqlalchemy.orm.base import NEVER_SET
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.properties import RelationshipProperty
from sqlalchemy.types import Enum, SchemaType, TypeDecorator
import requests.exceptions
import rpm

from bodhi.messages.schemas import buildroot_override as override_schemas
from bodhi.messages.schemas import errata as errata_schemas
from bodhi.messages.schemas import update as update_schemas
from bodhi.server import bugs, buildsys, log, mail, notifications, Session, util
from bodhi.server.config import config
from bodhi.server.exceptions import (
    BodhiException,
    ExternalCallException,
    LockedUpdateException,
)
from bodhi.server.tasks import (
    fetch_test_cases_task,
    tag_update_builds_task,
    work_on_bugs_task,
)
from bodhi.server.util import avatar as get_avatar
from bodhi.server.util import (
    build_evr,
    get_critpath_components,
    get_grouped_critpath_components,
    get_rpm_header,
    header,
    pagure_api_get,
    build_names_by_type,
    markdown_to_text,
    wrap_text,
)


if typing.TYPE_CHECKING:  # pragma: no cover
    import bugzilla  # noqa: 401
    import pyramid  # noqa: 401


# http://techspot.zzzeek.org/2011/01/14/the-enum-recipe

class EnumSymbol(object):
    """Define a fixed symbol tied to a parent class."""

    def __init__(self, cls_, name, value, description):
        """
        Initialize the EnumSymbol.

        Args:
            cls_ (EnumMeta): The metaclass this symbol is tied to.
            name (str): The name of this symbol.
            value (str): The value used in the database to represent this symbol.
            description (str): A human readable description of this symbol.
        """
        self.cls_ = cls_
        self.name = name
        self.value = value
        self.description = description

    def __lt__(self, other):
        """
        Return True if self.value is less than other.value.

        Args:
            other (EnumSymbol): The other EnumSymbol we are being compared to.
        Returns:
            bool: True if self.value is less than other.value, False otherwise.
        """
        return self.value < other.value

    def __reduce__(self):
        """
        Allow unpickling to return the symbol linked to the DeclEnum class.

        Returns:
            tuple: A 2-tuple of the ``getattr`` function, and a 2-tuple of the EnumSymbol's member
            class and name.
        """
        return getattr, (self.cls_, self.name)

    def __iter__(self):
        """
        Iterate over this EnumSymbol's value and description.

        Returns:
            iterator: An iterator over the value and description.
        """
        return iter([self.value, self.description])

    def __repr__(self):
        """
        Return a string representation of this EnumSymbol.

        Returns:
            str: A string representation of this EnumSymbol's value.
        """
        return "<%s>" % self.name

    def __str__(self) -> str:
        """
        Return a string representation of this EnumSymbol.

        Returns:
            A string representation of this EnumSymbol's value.
        """
        return str(self.value)

    def __json__(self, request=None):
        """
        Return a JSON representation of this EnumSymbol.

        Args:
            request (pyramid.request.Request): The current request.
        Returns:
            str: A string representation of this EnumSymbol's value.
        """
        return self.value


class EnumMeta(type):
    """Generate new DeclEnum classes."""

    def __init__(cls, classname, bases, dict_):
        """
        Initialize the metaclass.

        Args:
            classname (str): The name of the enum.
            bases (list): A list of base classes for the enum.
            dict_ (dict): A key-value mapping for the new enum's attributes.
        Returns:
            DeclEnum: A new DeclEnum.
        """
        cls._reg = reg = cls._reg.copy()
        for k, v in dict_.items():
            if isinstance(v, tuple) and v:
                sym = reg[v[0]] = EnumSymbol(cls, k, *v)
                setattr(cls, k, sym)
        return type.__init__(cls, classname, bases, dict_)

    def __iter__(cls):
        """
        Iterate the enum values.

        Returns:
            iterator: An iterator for the enum values.
        """
        return iter(cls._reg.values())


class DeclEnum(metaclass=EnumMeta):
    """Declarative enumeration."""

    _reg = {}

    @classmethod
    def from_string(cls, value):
        """
        Convert a string version of the enum to its enum type.

        Args:
            value (str): A string that you wish to convert to an Enum value.
        Returns:
            EnumSymbol: The symbol corresponding to the value.
        Raises:
            ValueError: If no symbol matches the given value.
        """
        try:
            return cls._reg[value]
        except KeyError:
            raise ValueError("Invalid value for %r: %r" % (cls.__name__, value))

    @classmethod
    def values(cls):
        """
        Return the possible values that this enum can take on.

        Returns:
            list: A list of strings of the values that this enum can represent.
        """
        return list(cls._reg.keys())

    @classmethod
    def db_type(cls):
        """
        Return a database column type to be used for this enum.

        Returns:
            DeclEnumType: A DeclEnumType to be used for this enum.
        """
        return DeclEnumType(cls)


class DeclEnumType(SchemaType, TypeDecorator):
    """A database column type for an enum."""

    cache_ok = True
    """See ``sqlalchemy.types.TypeDecorator.cache_ok``"""

    def __init__(self, enum):
        """
        Initialize with the given enum.

        Args:
            enum (bodhi.server.models.EnumMeta): The enum metaclass.
        """
        self.enum = enum
        self.impl = Enum(
            *enum.values(),
            name="ck%s" % re.sub('([A-Z])', lambda m: "_" + m.group(1).lower(), enum.__name__),
            # Required for SQLAlchemy >= 1.3.8
            # https://docs.sqlalchemy.org/en/14/changelog/changelog_13.html#change-ac119f6307026142f7a0ccbf81065f25
            sort_key_function=lambda e: str(e),
        )

    def _set_table(self, table, column):
        """
        Set the table for this object.

        Args:
            table (sqlalchemy.sql.schema.Table): The table that uses this Enum.
            column (sqlalchemy.sql.schema.Column): The column that uses this Enum.
        """
        self.impl._set_table(table, column)

    def copy(self):
        """
        Return a copy of self.

        Returns:
            DeclEnumType: A copy of self.
        """
        return DeclEnumType(self.enum)

    def process_bind_param(self, value, dialect):
        """
        Return the value of the enum.

        Args:
            value (bodhi.server.models.enum.EnumSymbol): The enum symbol we are resolving the value
                of.
            dialect (sqlalchemy.engine.default.DefaultDialect): Unused.
        Returns:
            str: The EnumSymbol's value.
        """
        if value is None:
            return None

        if isinstance(value, str):
            return value
        return value.value

    def process_result_value(self, value, dialect):
        """
        Return the enum that matches the given string.

        Args:
            value (str): The name of an enum.
            dialect (sqlalchemy.engine.default.DefaultDialect): Unused.
        Returns:
            EnumSymbol or None: The enum that matches value, or ``None`` if ``value`` is ``None``.
        """
        if value is None:
            return None
        return self.enum.from_string(value.strip())

    def create(self, bind=None, checkfirst=False):
        """Issue CREATE ddl for this type, if applicable."""
        super(DeclEnumType, self).create(bind, checkfirst)
        t = self.dialect_impl(bind.dialect)
        if t.impl.__class__ is not self.__class__ and isinstance(t, SchemaType):
            t.impl.create(bind=bind, checkfirst=checkfirst)

    def drop(self, bind=None, checkfirst=False):
        """Issue DROP ddl for this type, if applicable."""
        super(DeclEnumType, self).drop(bind, checkfirst)
        t = self.dialect_impl(bind.dialect)
        if t.impl.__class__ is not self.__class__ and isinstance(t, SchemaType):
            t.impl.drop(bind=bind, checkfirst=checkfirst)


class TZDateTime(TypeDecorator):
    """
    A database column type to mock timezone aware DateTime.

    In Bodhi all times are considered UTC, so we store naive datetimes in db
    and always return aware datetimes in UTC.
    """

    impl = DateTime
    cache_ok = True
    """See ``sqlalchemy.types.TypeDecorator.cache_ok``"""

    def process_bind_param(self, value, dialect):
        """Convert time to UTC and store as naive."""
        if value is not None:
            if not value.tzinfo or value.tzinfo.utcoffset(value) is None:  # pragma: no cover
                raise TypeError("tzinfo is required")
            value = value.astimezone(timezone.utc).replace(tzinfo=None)
        return value

    def process_result_value(self, value, dialect):
        """Return datetime with UTC timezone."""
        if value is not None:
            value = value.replace(tzinfo=timezone.utc)
        return value


class BodhiBase(object):
    """
    Base class for the SQLAlchemy model base class.

    Attributes:
        __exclude_columns__ (tuple): A list of columns to exclude from JSON
        __include_extras__ (tuple): A list of methods or attrs to include in JSON
        __get_by__ (tuple): A list of columns that :meth:`.get` will query.
        id (int): An integer id that serves as the default primary key.
        query (sqlalchemy.orm.query.Query): a class property which produces a
            Query object against the class and the current Session when called.
    """

    __exclude_columns__ = ('id',)
    __include_extras__ = tuple()
    __get_by__ = ()

    id = Column(Integer, primary_key=True)

    query = Session.query_property()

    @classmethod
    def get(cls, id):
        """
        Return an instance of the model by using its __get_by__ attribute with id.

        Args:
            id (object): An attribute to look up the model by.
        Returns:
            BodhiBase or None: An instance of the model that matches the id, or ``None`` if no match
            was found.
        """
        return cls.query.filter(or_(
            getattr(cls, col) == id for col in cls.__get_by__
        )).first()

    def __getitem__(self, key):
        """
        Define a dictionary like interface for the models.

        Args:
            key (string): The name of an attribute you wish to retrieve from the model.
        Returns:
            object: The value of the attribute represented by key.
        """
        return getattr(self, key)

    def __repr__(self):
        """
        Return a string representation of this model.

        Returns:
            str: A string representation of this model.
        """
        return '<{0} {1}>'.format(self.__class__.__name__, self.__json__())

    def __json__(self, request=None, exclude=None, include=None):
        """
        Return a JSON representation of this model.

        Args:
            request (pyramid.request.Request or None): The current web request, or None.
            exclude (iterable or None): An iterable of strings naming the attributes to exclude from
                the JSON representation of the model. If None (the default), the class's
                __exclude_columns__ attribute will be used.
            include (iterable or None): An iterable of strings naming the extra attributes to
                include in the JSON representation of the model. If None (the default), the class's
                __include_extras__ attribute will be used.
        Returns:
            dict: A dict representation of the model suitable for serialization as JSON.
        """
        return self._to_json(self, request=request, exclude=exclude, include=include)

    @classmethod
    def _to_json(cls, obj, seen=None, request=None, exclude=None, include=None):
        """
        Return a JSON representation of obj.

        Args:
            obj (BodhiBase): The model to serialize.
            seen (list or None): A list of attributes we have already serialized. Used by this
                method to keep track of its state, as it uses recursion.
            request (pyramid.request.Request or None): The current web request, or None.
            exclude (iterable or None): An iterable of strings naming the attributes to exclude from
                the JSON representation of the model. If None (the default), the class's
                __exclude_columns__ attribute will be used.
            include (iterable or None): An iterable of strings naming the extra attributes to
                include in the JSON representation of the model. If None (the default), the class's
                __include_extras__ attribute will be used.
        Returns:
            dict: A dict representation of the model suitable for serialization.
        """
        if not seen:
            seen = []
        if not obj:
            return

        if exclude is None:
            exclude = getattr(obj, '__exclude_columns__', [])
        properties = list(class_mapper(type(obj)).iterate_properties)
        rels = [p.key for p in properties if isinstance(p, RelationshipProperty)]
        attrs = [p.key for p in properties if p.key not in rels]
        d = dict([(attr, getattr(obj, attr)) for attr in attrs
                  if attr not in exclude and not attr.startswith('_')])

        if include is None:
            include = getattr(obj, '__include_extras__', [])

        for name in include:
            attribute = getattr(obj, name)
            if callable(attribute):
                attribute = attribute(request)
            d[name] = attribute

        for attr in rels:
            if attr in exclude:
                continue
            target = getattr(type(obj), attr).property.mapper.class_
            if target in seen:
                continue
            d[attr] = cls._expand(obj, getattr(obj, attr), seen, request)

        for key, value in d.items():

            if isinstance(value, datetime):
                d[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, date):
                d[key] = value.isoformat()
            if isinstance(value, EnumSymbol):
                d[key] = str(value)

        return d

    @classmethod
    def _expand(cls, obj, relation, seen, req):
        """
        Return the to_json or id of a sqlalchemy relationship.

        Args:
            obj (BodhiBase): The object we are trying to describe a relationship on.
            relation (object): A relationship attribute on obj we are trying to learn about.
            seen (list): A list of objects we have already recursed over.
            req (pyramid.request.Request): The current request.
        Returns:
            object: The to_json() or the id of a sqlalchemy relationship.
        """
        if hasattr(relation, 'all'):
            relation = relation.all()
        if hasattr(relation, '__iter__'):
            return [cls._expand(obj, item, seen, req) for item in relation]
        if type(relation) not in seen:
            return cls._to_json(relation, seen + [type(obj)], req)
        else:
            return relation.id

    @classmethod
    def grid_columns(cls):
        """
        Return the column names for the model, except for the excluded ones.

        Returns:
            list: A list of column names, with excluded ones removed.
        """
        columns = []
        exclude = getattr(cls, '__exclude_columns__', [])
        for col in cls.__table__.columns:
            if col.name in exclude:
                continue
            columns.append(col.name)
        return columns

    @classmethod
    def find_polymorphic_child(cls, identity):
        """
        Find a child of a polymorphic base class.

        For example, given the base Package class and the 'rpm' identity, this
        class method should return the RpmPackage class.

        This is accomplished by iterating over all classes in scope.
        Limiting that to only those which are an extension of the given base
        class.  Among those, return the one whose polymorphic_identity matches
        the value given.  If none are found, then raise a NameError.

        Args:
            identity (EnumSymbol): An instance of EnumSymbol used to identify the child.
        Returns:
            BodhiBase: The type-specific child class.
        Raises:
            KeyError: If this class is not polymorphic.
            NameError: If no child class is found for the given identity.
            TypeError: If identity is not an EnumSymbol.
        """
        if not isinstance(identity, EnumSymbol):
            raise TypeError("%r is not an instance of EnumSymbol" % identity)

        if 'polymorphic_on' not in getattr(cls, '__mapper_args__', {}):
            raise KeyError("%r is not a polymorphic model." % cls)

        classes = (c for c in globals().values() if isinstance(c, type))
        children = (c for c in classes if issubclass(c, cls))
        for child in children:
            candidate = child.__mapper_args__.get('polymorphic_identity')
            if candidate is identity:
                return child

        error = "Found no child of %r with identity %r"
        raise NameError(error % (cls, identity))


Base = declarative_base(cls=BodhiBase)
metadata = Base.metadata


##
#  Enumerated type declarations
##
class ContentType(DeclEnum):
    """
    Used to differentiate between different kinds of content in various models.

    This enum is used to mark objects as pertaining to particular kinds of content type, such as
    RPMs or Modules.

    Attributes:
        base (EnumSymbol): This is used to represent base classes that are shared between specific
            content types.
        rpm (EnumSymbol): Used to represent RPM related objects.
        module (EnumSymbol): Used to represent Module related objects.
        container (EnumSymbol): Used to represent Container related objects.
        flatpak (EnumSymbol): Used to represent Flatpak related objects.
    """

    base = 'base', 'Base'
    rpm = 'rpm', 'RPM'
    module = 'module', 'Module'
    container = 'container', 'Container'
    flatpak = 'flatpak', 'Flatpak'

    @classmethod
    def infer_content_class(cls, base, build):
        """
        Identify and return the child class associated with the appropriate ContentType.

        For example, given the Package base class and a normal koji build, return
        the RpmPackage model class. Or, given the Build base class and a container
        build, return the ContainerBuild model class.

        Args:
            base (BodhiBase): A base model class, such as :class:`Build` or :class:`Package`.
            build (dict): Information about the build from the build system (koji).
        Returns:
            BodhiBase: The type-specific child class of base that is appropriate to use with the
            given koji build.
        Raises:
            ValueError: If there is no appropriate child class
        """
        # Default value.  Overridden below if we find markers in the build info
        identity = cls.rpm

        extra = build.get('extra') or {}
        if 'module' in extra.get('typeinfo', {}):
            identity = cls.module
        elif 'image' in extra.get('typeinfo', {}):
            image_info = extra['typeinfo']['image']
            if 'pull' not in image_info.get('index', {}):
                raise ValueError(
                    (f"Image build {build['nvr']} cannot be used for update, "
                     "it has no pull specs")
                )
            if 'flatpak' in image_info:
                identity = cls.flatpak
            else:
                identity = cls.container

        return base.find_polymorphic_child(identity)


class UpdateStatus(DeclEnum):
    """
    An enum used to describe the current state of an update.

    Attributes:
        pending (EnumSymbol): The update is not in any repository.
        testing (EnumSymbol): The update is in the testing repository.
        stable (EnumSymbol): The update is in the stable repository.
        unpushed (EnumSymbol): The update had been in a testing repository, but has been removed.
        obsolete (EnumSymbol): The update has been obsoleted by another update.
    """

    pending = 'pending', 'pending'
    testing = 'testing', 'testing'
    stable = 'stable', 'stable'
    unpushed = 'unpushed', 'unpushed'
    obsolete = 'obsolete', 'obsolete'


class TestGatingStatus(DeclEnum):
    """
    This class lists the different status the ``Update.test_gating_status`` flag can have.

    Attributes:
        waiting (EnumSymbol): Bodhi is waiting to hear about the test gating status of the update.
        ignored (EnumSymbol): Greenwave said that the update does not require any tests.
        queued (EnumSymbol): Greenwave said that the required tests for this update have been
            queued.
        running (EnumSymbol): Greenwave said that the required tests for this update are running.
        passed (EnumSymbol): Greenwave said that the required tests for this update have passed.
        failed (EnumSymbol): Greenwave said that the required tests for this update have failed.
    """

    waiting = 'waiting', 'Waiting'
    ignored = 'ignored', 'Ignored'
    queued = 'queued', 'Queued'
    running = 'running', 'Running'
    passed = 'passed', 'Passed'
    failed = 'failed', 'Failed'
    greenwave_failed = 'greenwave_failed', 'Greenwave failed to respond'


class UpdateType(DeclEnum):
    """
    An enum used to classify the type of the update.

    Attributes:
        bugfix (EnumSymbol): The update fixes bugs only.
        security (EnumSymbol): The update addresses security issues.
        newpackage (EnumSymbol): The update introduces new packages to the release.
        enhancement (EnumSymbol): The update introduces new features.
    """

    bugfix = 'bugfix', 'bugfix'
    security = 'security', 'security'
    newpackage = 'newpackage', 'newpackage'
    enhancement = 'enhancement', 'enhancement'
    unspecified = 'unspecified', 'unspecified'


class UpdateRequest(DeclEnum):
    """
    An enum used to specify an update requesting to change states.

    Attributes:
        testing (EnumSymbol): The update is requested to change to testing.
        obsolete (EnumSymbol): The update has been obsoleted by another update.
        unpush (EnumSymbol): The update no longer needs to be released.
        revoke (EnumSymbol): The unpushed update will no longer be composed in any repository.
        stable (EnumSymbol): The update is ready to be pushed to the stable repository.
    """

    testing = 'testing', 'testing'
    obsolete = 'obsolete', 'obsolete'
    unpush = 'unpush', 'unpush'
    revoke = 'revoke', 'revoke'
    stable = 'stable', 'stable'


class UpdateSeverity(DeclEnum):
    """
    An enum used to specify the severity of the update.

    Attributes:
        unspecified (EnumSymbol): The packager has not specified a severity.
        urgent (EnumSymbol): The update is urgent.
        high (EnumSymbol): The update is high severity.
        medium (EnumSymbol): The update is medium severity.
        low (EnumSymbol): The update is low severity.
    """

    unspecified = 'unspecified', 'unspecified'
    urgent = 'urgent', 'urgent'
    high = 'high', 'high'
    medium = 'medium', 'medium'
    low = 'low', 'low'


class UpdateSuggestion(DeclEnum):
    """
    An enum used to tell the user whether they need to reboot or logout after applying an update.

    Attributes:
        unspecified (EnumSymbol): No action is needed.
        reboot (EnumSymbol): The user should reboot after applying the update.
        logout (EnumSymbol): The user should logout after applying the update.
    """

    unspecified = 'unspecified', 'unspecified'
    reboot = 'reboot', 'reboot'
    logout = 'logout', 'logout'


class ReleaseState(DeclEnum):
    """
    An enum that describes the state of a :class:`Release`.

    Attributes:
        disabled (EnumSymbol): Indicates that the release is disabled.
        pending (EnumSymbol): Indicates that the release is pending.
        frozen (EnumSymbol): Indicates that the release is frozen.
        current (EnumSymbol): Indicates that the release is current.
        archived (EnumSymbol): Indicates that the release is archived.
    """

    disabled = 'disabled', 'disabled'
    pending = 'pending', 'pending'
    frozen = 'frozen', 'frozen'
    current = 'current', 'current'
    archived = 'archived', 'archived'


class ComposeState(DeclEnum):
    """
    Define the various states that a :class:`Compose` can be in.

    Attributes:
        requested (EnumSymbol): A compose has been requested, but it has not started yet.
        pending (EnumSymbol): The request for the compose has been received by the backend worker,
            but the compose has not started yet.
        initializing (EnumSymbol): The compose is initializing.
        updateinfo (EnumSymbol): The updateinfo.xml is being generated.
        punging (EnumSymbol): A Pungi soldier has been deployed to deal with the situation.
        syncing_repo (EnumSymbol): The repo is being synced to the master mirror.
        notifying (EnumSymbol): Pungi has finished successfully, and we are now sending out various
            forms of notifications, such as e-mail, bus messages, and bugzilla.
        success (EnumSymbol): The Compose has completed successfully.
        failed (EnumSymbol): The compose has failed, abandon hope.
        signing_repo (EnumSymbol): Waiting for the repo to be signed.
        cleaning (EnumSymbol): Cleaning old Composes after successful completion.
    """

    requested = 'requested', 'Requested'
    pending = 'pending', 'Pending'
    initializing = 'initializing', 'Initializing'
    updateinfo = 'updateinfo', 'Generating updateinfo.xml'
    punging = 'punging', 'Waiting for Pungi to finish'
    syncing_repo = 'syncing_repo', 'Wait for the repo to hit the master mirror'
    notifying = 'notifying', 'Sending notifications'
    success = 'success', 'Success'
    failed = 'failed', 'Failed'
    signing_repo = 'signing_repo', 'Signing repo'
    cleaning = 'cleaning', 'Cleaning old composes'


class PackageManager(DeclEnum):
    """
    An enum used to specify what package manager is used by a specific Release.

    Attributes:
        unspecified (EnumSymbol): for releases where the package manager is not specified.
        dnf (EnumSymbol): DNF package manager.
        yum (EnumSymbol): YUM package manager.
    """

    unspecified = 'unspecified', 'package manager not specified'
    dnf = 'dnf', 'dnf'
    yum = 'yum', 'yum'


##
#  Association tables
##

update_bug_table = Table(
    'update_bug_table', metadata,
    Column('update_id', Integer, ForeignKey('updates.id')),
    Column('bug_id', Integer, ForeignKey('bugs.id')))


build_testcase_table = Table(
    'build_testcase_table', metadata,
    Column('build_id', Integer, ForeignKey('builds.id')),
    Column('testcase_id', Integer, ForeignKey('testcases.id')))


class Release(Base):
    """
    Represent a distribution release, such as Fedora 27.

    Attributes:
        name (str): The name of the release, such as 'F27'.
        long_name (str): A human readable name for the release, such as 'Fedora 27'.
        version (str): The version of the release, such as '27'.
        id_prefix (str): The prefix to use when forming update aliases for this release, such as
            'FEDORA'.
        branch (str): The dist-git branch associated with this release, such as 'f27'.
        dist_tag (str): The koji dist_tag associated with this release, such as 'f27'.
        stable_tag (str): The koji tag to be used for stable builds in this release, such as
            'f27-updates'.
        testing_tag (str): The koji tag to be used for testing builds in this release, such as
            'f27-updates-testing'.
        candidate_tag (str): The koji tag used for builds that are candidates to be updates,
            such as 'f27-updates-candidate'.
        pending_signing_tag (str): The koji tag that specifies that a build is waiting to be
            signed, such as 'f27-signing-pending'.
        pending_testing_tag (str): The koji tag that indicates that a build is waiting to be
            composed into the testing repository, such as 'f27-updates-testing-pending'.
        pending_stable_tag (str): The koji tag that indicates that a build is waiting to be
            composed into the stable repository, such as 'f27-updates-pending'.
        override_tag (str): The koji tag that is used when a build is added as a buildroot
            override, such as 'f27-override'.
        mail_template (str): The notification mail template.
        state (:class:`ReleaseState`): The current state of the release. Defaults to
            ``ReleaseState.disabled``.
        builds (sqlalchemy.orm.collections.InstrumentedList): An iterable of :class:`Builds <Build>`
            associated with this release.
        composed_by_bodhi (bool): The flag that indicates whether the release is composed by
            Bodhi or not. Defaults to True.
        create_automatic_updates (bool): A flag indicating that updates should
            be created automatically for Koji builds tagged into the
            ``candidate_tag``. Defaults to False.
        package_manager (EnumSymbol): The package manager this release uses. This must be one of
            the values defined in :class:`PackageManager`.
        testing_repository (str): The name of repository where updates are placed for
            testing before being pushed to the main repository.
        released_on (str): Date of first release in a datetime.date() format '2020-05-17'.
        eol (str): End-of-life of the release in a datetime.date() format '2020-05-17'.
    """

    __tablename__ = 'releases'
    __exclude_columns__ = ('id', 'builds', 'composes')
    __include_extras__ = ('setting_status', )
    __get_by__ = ('name', 'long_name', 'dist_tag')

    name = Column(Unicode(10), unique=True, nullable=False)
    long_name = Column(Unicode(25), unique=True, nullable=False)
    version = Column(Unicode(5), nullable=False)
    id_prefix = Column(Unicode(25), nullable=False)
    branch = Column(Unicode(10), nullable=False)

    dist_tag = Column(Unicode(20), nullable=False)
    stable_tag = Column(UnicodeText, nullable=False)
    testing_tag = Column(UnicodeText, nullable=False)
    candidate_tag = Column(UnicodeText, nullable=False)
    pending_signing_tag = Column(UnicodeText, nullable=False)
    pending_testing_tag = Column(UnicodeText, nullable=False)
    pending_stable_tag = Column(UnicodeText, nullable=False)
    override_tag = Column(UnicodeText, nullable=False)
    mail_template = Column(UnicodeText, default='fedora_errata_template', nullable=False)

    state = Column(ReleaseState.db_type(), default=ReleaseState.disabled, nullable=False)
    composed_by_bodhi = Column(Boolean, default=True)
    create_automatic_updates = Column(Boolean, default=False)

    _version_int_regex = re.compile(r'\D+(\d+)[CMFN]?$')

    package_manager = Column(PackageManager.db_type(), default=PackageManager.unspecified)
    testing_repository = Column(UnicodeText, nullable=True)
    released_on = Column(Date, nullable=True)
    eol = Column(Date, nullable=True)

    # One-to-many relationships
    builds = relationship('Build', back_populates='release')
    composes = relationship('Compose', back_populates='release')

    @property
    def min_karma(self) -> int:
        """
        Return the min_karma for updates for this release.

        If the release doesn't specify a min_karma, the default min_karma setting is used
        instead.

        Returns:
            The minimum karma required for updates for this release.
        """
        if self.setting_status:
            min_karma = config.get(
                f'{self.setting_prefix}.{self.setting_status}.min_karma', None)
            if min_karma:
                return int(min_karma)
        return config.get('min_karma')

    @property
    def version_int(self):
        """
        Return an integer representation of the version of this release.

        Returns:
            int: The version of the release.
        """
        return int(self._version_int_regex.match(self.name).groups()[0])

    @property
    def mandatory_days_in_testing(self):
        """
        Return the number of days that updates in this release must spend in testing.

        Returns:
            int: The number of days in testing that updates in this release must spend in
            testing. If the release isn't configured to have mandatory testing time, 0 is
            returned.
        """
        if self.setting_status:
            days = config.get(f'{self.setting_prefix}.{self.setting_status}'
                              f'.mandatory_days_in_testing', None)
        else:
            days = config.get(f'{self.id_prefix.lower().replace("-", "_")}'
                              f'.mandatory_days_in_testing', None)
        if days is None:
            log.warning(f'No mandatory days in testing defined for {self.name}. Defaulting to 0.')
            return 0
        else:
            return int(days)

    @property
    def critpath_mandatory_days_in_testing(self):
        """
        Return the number of days that critpath updates in this release must spend in testing.

        Returns:
            int: The number of days in testing that critpath updates in this release must spend in
            testing. If the release isn't configured to have critpath mandatory testing time, 0 is
            returned.
        """
        if self.setting_status:
            days = config.get(f'{self.setting_prefix}.{self.setting_status}'
                              f'.critpath.mandatory_days_in_testing', None)
            if days is not None:
                return int(days)

        return config.get('critpath.mandatory_days_in_testing', 0)

    @property
    def collection_name(self):
        """
        Return the collection name of this release (eg: Fedora EPEL).

        Returns:
            str: The collection name of this release.
        """
        return ' '.join(self.long_name.split()[:-1])

    @classmethod
    @lru_cache(maxsize=1)
    def all_releases(cls):
        """
        Return a mapping of release states to a list of dictionaries describing the releases.

        Returns:
            defaultdict: Mapping strings of :class:`ReleaseState` names to lists of dictionaries
            that describe the releases in those states.
        """
        releases = defaultdict(list)
        for release in cls.query.order_by(cls.name.desc()).all():
            releases[release.state.value].append(release.__json__())
        return releases

    @classmethod
    @lru_cache(maxsize=1)
    def get_tags(cls):
        """
        Return a 2-tuple mapping tags to releases.

        Returns:
            tuple: A 2-tuple. The first element maps the keys 'candidate', 'testing', 'stable',
            'override', 'pending_testing', and 'pending_stable' each to a list of tags for various
            releases that correspond to those tag semantics. The second element maps each koji tag
            to the release's name that uses it.
        """
        data = {'candidate': [], 'testing': [], 'stable': [], 'override': [],
                'pending_testing': [], 'pending_stable': []}
        tags = {}  # tag -> release lookup
        for release in cls.query.filter(cls.state.notin_([ReleaseState.archived,
                                                          ReleaseState.disabled])).all():
            for key in data:
                tag = getattr(release, f'{key}_tag')
                data[key].append(tag)
                tags[tag] = release.name
        return (data, tags)

    @classmethod
    def from_tags(cls, tags, session):
        """
        Find a release associated with one of the given koji tags.

        Args:
            tags (list): A list of koji tags for which an associated release is desired.
            session (sqlalchemy.orm.session.Session): A database session.
        Returns:
            Release or None: The first release found that matches the first tag. If no release is
                found, ``None`` is returned.
        """
        tag_types, tag_rels = cls.get_tags()
        for tag in tags:
            if tag not in tag_rels:
                continue
            release = session.query(cls).filter_by(name=tag_rels[tag]).first()
            if release:
                return release

    @property
    def setting_prefix(self) -> str:
        """
        Return the prefix for settings that pertain to this Release.

        Returns:
            The Release's setting prefix.
        """
        return self.name.lower().replace('-', '')

    @property
    def setting_status(self) -> typing.Optional[str]:
        """
        Return the status of the Release from settings.

        Return the Release's status setting from the config. For example, if the release is f30,
        this will return the value of f30.status from the config file.

        Note: This is not the same as Release.state.

        Returns:
            The status of the release.
        """
        return config.get(f'{self.setting_prefix}.status', None)

    def get_pending_testing_side_tag(self, from_tag: str) -> str:
        """
        Return the testing-pending side tag for this ``Release``.

        Args:
            from_tag: Name of side tag from which ``Update`` was created.

        Returns:
            Testing-pending side tag used in koji.
        """
        side_tag_postfix = config.get(
            f'{self.setting_prefix}.koji-testing-side-tag', "-testing-pending")
        return from_tag + side_tag_postfix

    def get_pending_signing_side_tag(self, from_tag: str) -> str:
        """
        Return the signing-pending side tag for this ``Release``.

        Args:
            from_tag: Name of side tag from which ``Update`` was created.

        Returns:
            Signing-pending side tag used in koji.
        """
        side_tag_postfix = config.get(
            f'{self.setting_prefix}.koji-signing-pending-side-tag', "-signing-pending")
        return from_tag + side_tag_postfix

    @property
    def inherited_override_tags(self) -> list:
        """
        Return the override tags inherited from other Releases.

        The override tags inheritance is configured by defining the list of
        Releases we should extend from in the config file the same way of setting_prefix.
        For example, if the release is epel9-n using epel-9.override-extend=EPEL-9N,EPEL-8
        will make this method to return the override tag set for EPEL-9N and EPEL-8.

        Note: pay attention, 'epel-9.override-extend' uses the release name in lowercase,
        while the list of releases should match the release names case sensitive.

        Returns:
            A list of override tags inherited from other releases.
        """
        tags = []
        inheritance = config.get(f'{self.setting_prefix}.override-extend', None)
        if inheritance is not None:
            rel_list = [Release.get(name.strip()) for name in inheritance.split(',')]
            for rel in rel_list:
                if rel is not None:
                    tags.append(rel.override_tag)
        return list(filter(None, tags))


class TestCase(Base):
    """
    Represents test cases from the wiki.

    Attributes:
        name (str): The name of the test case.
        package_name (str): The name of the package associated with this test case.
    """

    __tablename__ = 'testcases'
    __get_by__ = ('name',)
    __exclude_columns__ = ('builds', 'feedback')

    name = Column(UnicodeText, nullable=False, unique=True)

    # One-to-many relationships
    feedback = relationship('TestCaseKarma', back_populates='testcase')

    # Many-to-many relationships
    builds = relationship('Build', secondary=build_testcase_table,
                          back_populates='testcases')


class Package(Base):
    """
    This model represents a package.

    This model uses single-table inheritance to allow for different package types.

    Attributes:
        name (str): A text string that uniquely identifies the package.
        type (int): The polymorphic identity column. This is used to identify what Python
            class to create when loading rows from the database.
        builds (sqlalchemy.orm.collections.InstrumentedList): A list of :class:`Build` objects.
    """

    __tablename__ = 'packages'
    __get_by__ = ('name',)
    __exclude_columns__ = ('id', 'builds',)

    name = Column(UnicodeText, nullable=False)
    type = Column(ContentType.db_type(), nullable=False)

    # One-to-many relationships
    builds = relationship('Build', back_populates='package')

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': ContentType.base,
    }

    __table_args__ = (
        UniqueConstraint('name', 'type', name='packages_name_and_type_key'),
    )

    @property
    def external_name(self):
        """
        Return the package name as it's known to external services.

        For most Packages, this is self.name.

        Returns:
            str: The name of this package.
        """
        return self.name

    def get_pkg_committers_from_pagure(self):
        """
        Pull users and groups who can commit on a package in Pagure.

        Returns a tuple with two lists:
        * The first list contains usernames that have commit access.
        * The second list contains FAS group names that have commit access.

        Raises:
            RuntimeError: If Pagure did not give us a 200 code.
        """
        pagure_url = config.get('pagure_url')
        namespace = config.get('pagure_namespaces')[self.type.name]
        package_pagure_url = '{0}/api/0/{1}/{2}?expand_group=1'.format(
            pagure_url.rstrip('/'), namespace, self.external_name)
        package_json = pagure_api_get(package_pagure_url)

        committers = set()
        for access_type in ['owner', 'admin', 'commit']:
            committers = committers | set(
                package_json['access_users'][access_type])

        groups = set()
        for access_type in ['admin', 'commit']:
            for group_name in package_json['access_groups'][access_type]:
                groups.add(group_name)
                # Add to the list of committers the users in the groups
                # having admin or commit access
                committers = committers | set(
                    package_json.get(
                        'group_details', {}).get(group_name, []))

        # The first list contains usernames with commit access. The second list
        # contains FAS group names with commit access.
        return list(committers), list(groups)

    def hascommitaccess(self, username: str, branchname: str) -> bool:
        """
        Check on Pagure if a user has commit access on the package/branch.

        Raises:
            RuntimeError: If Pagure did not give us a 200 code.
        """
        pagure_url = config.get('pagure_url')
        namespace = config.get('pagure_namespaces')[self.type.name]
        # Here we override the queried branchname because:
        # - flatpaks only have one main branch
        # - modules streams have no direct mapping to branch names
        # The effect is that we cannot check collaborators rights for specific
        # streams on modules, so we fall back to old Bodhi behavior
        if self.type == ContentType.flatpak:
            branchname = config.get('pagure_flatpak_main_branch')
        elif self.type == ContentType.module:
            branchname = config.get('pagure_module_main_branch')

        pagure_query_url = (f'{pagure_url.rstrip("/")}/api/0/{namespace}/{self.external_name}'
                            f'/hascommit?user={username}&branch={branchname}')
        pagure_response = pagure_api_get(pagure_query_url)
        return pagure_response['hascommit']

    @validates('builds', include_backrefs=True)
    def validate_builds(self, key, build):
        """
        Validate builds being appended to ensure they are all the same type as the Package.

        This method checks to make sure that all the builds on self.builds have their type attribute
        equal to self.type. The goal is to make sure that Builds of a specific type are only ever
        associated with Packages of the same type and vice-versa. For example, RpmBuilds should only
        ever associate with RpmPackages and never with ModulePackages.

        Args:
            key (str): The field's key, which is un-used in this validator.
            build (Build): The build object which was appended to the list
                of builds.

        Raises:
            ValueError: If the build being appended is not the same type as the package.
        """
        if build.type != self.type:
            raise ValueError(
                ("A {} Build cannot be associated with a {} Package. A Package's builds must be "
                 "the same type as the package.").format(
                     build.type.description, self.type.description))
        return build

    def __str__(self):
        """
        Return a string representation of the package.

        Returns:
            str: A string representing this package.
        """
        x = header(self.name)
        states = {'pending': [], 'testing': [], 'stable': []}
        if self.builds:
            for build in self.builds:
                if build.update and build.update.status.description in states:
                    states[build.update.status.description].append(
                        build.update)
        for state in states:
            if states[state]:
                x += "\n %s Updates (%d)\n" % (state.title(),
                                               len(states[state]))
                for update in states[state]:
                    x += "    o %s\n" % update.get_title()
        del states
        return x

    @staticmethod
    def _get_name(build):
        """
        Determine the package name for a particular build.

        For most builds, this will return the RPM name, unless overridden in a specific
        subclass.

        Args:
            build (dict): Information about the build from the build system (koji).
        Returns:
            str: The Package object identifier for this build.
        """
        name, _, _ = build['nvr']
        return name

    @staticmethod
    def check_existence(build):
        """
        Check if the Package instance associated with the build is already in database.

        Args:
            build (dict): Information about the build from the build system (koji).
        Returns:
            bool: True if the type-specific instance of Package is alreadi in database.
        """
        base = ContentType.infer_content_class(Package, build['info'])
        name = base._get_name(build)
        package = base.query.filter_by(name=name).one_or_none()
        if not package:
            return False
        return True

    @staticmethod
    def get_or_create(session, build):
        """
        Identify and return the Package instance associated with the build.

        For example, given a normal koji build, return a RpmPackage instance.
        Or, given a container, return a ContainerBuild instance.

        Args:
            session (sqlalchemy.orm.session.Session): A database session.
            build (dict): Information about the build from the build system (koji).
        Returns:
            Package: A type-specific instance of Package for the specific build requested.
        """
        base = ContentType.infer_content_class(Package, build['info'])
        name = base._get_name(build)
        package = base.query.filter_by(name=name).one_or_none()
        if not package:
            package = base(name=name)
            session.add(package)
            session.flush()
        return package


class ContainerPackage(Package):
    """Represents a Container package."""

    __mapper_args__ = {
        'polymorphic_identity': ContentType.container,
    }


class FlatpakPackage(Package):
    """Represents a Flatpak package."""

    __mapper_args__ = {
        'polymorphic_identity': ContentType.flatpak,
    }


class ModulePackage(Package):
    """Represents a Module package."""

    __mapper_args__ = {
        'polymorphic_identity': ContentType.module,
    }

    @property
    def external_name(self):
        """
        Return the package name as it's known to external services.

        For modules, this splits the :stream portion back off.

        Returns:
            str: The name of this module package without :stream.
        """
        return self.name.split(':')[0]

    @staticmethod
    def _get_name(build):
        """
        Determine the name:stream for a particular module build.

        Args:
            build (dict): Information about the build from the build system (koji).
        Returns:
            str: The name:stream of this module build.
        """
        name, stream, _ = build['nvr']
        return '%s:%s' % (name, stream)


class RpmPackage(Package):
    """Represents a RPM package."""

    __mapper_args__ = {
        'polymorphic_identity': ContentType.rpm,
    }


class Build(Base):
    """
    This model represents a specific build of a package.

    This model uses single-table inheritance to allow for different build types.

    Attributes:
        nvr (str): The nvr field is really a mapping to the Koji build_target.name field, and is
            used to reference builds in Koji. It is named nvr in reference to the dash-separated
            name-version-release Koji name for RPMs, but it is used by other types as well. At the
            time of this writing, it was not practical to rename nvr since it is used in the REST
            API to reference builds. Thus, it should be thought of as a Koji build identifier rather
            than strictly as an RPM's name, version, and release.
        package_id (int): A foreign key to the Package that this Build is part of.
        release_id (int): A foreign key to the Release that this Build is part of.
        signed (bool): If True, this package has been signed by robosignatory. If False, it has not
            been signed yet.
        update_id (int): A foreign key to the Update that this Build is part of.
        release (sqlalchemy.orm.relationship): A relationship to the Release that this build is part
            of.
        type (ContentType): The polymorphic identify of the row. This is used by sqlalchemy to
            identify which subclass of Build to use.
        testcases (sqlalchemy.orm.collections.InstrumentedList): A list of :class:`TestCase`
            objects.
    """

    __tablename__ = 'builds'
    __exclude_columns__ = ('id', 'package', 'package_id', 'release', 'testcases',
                           'update_id', 'update', 'override')
    __get_by__ = ('nvr',)

    nvr = Column(Unicode(100), unique=True, nullable=False)
    signed = Column(Boolean, default=False, nullable=False)

    # One-to-many relationships
    override = relationship('BuildrootOverride', back_populates='build', uselist=False)

    # Many-to-one relationships
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    package = relationship('Package', back_populates='builds', lazy='joined', innerjoin=True)

    release_id = Column(Integer, ForeignKey('releases.id'))
    release = relationship('Release', back_populates='builds', lazy=False)

    update_id = Column(Integer, ForeignKey('updates.id'), index=True)
    update = relationship('Update', back_populates='builds')

    # Many-to-many relationships
    testcases = relationship('TestCase', secondary=build_testcase_table,
                             back_populates='builds', order_by='TestCase.name')

    type = Column(ContentType.db_type(), nullable=False)
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': ContentType.base,
    }

    def _get_kojiinfo(self):
        """
        Return Koji build info about this build, from a cache if possible.

        Returns:
            dict: The response from Koji's getBuild() for this Build.
        """
        if not hasattr(self, '_kojiinfo'):
            koji_session = buildsys.get_session()
            self._kojiinfo = koji_session.getBuild(self.nvr)
        return self._kojiinfo

    def _get_n_v_r(self):
        """
        Return the N, V and R components for a traditionally dash-separated build.

        Returns:
            tuple: A 3-tuple of name, version, release.
        """
        return self.nvr.rsplit('-', 2)

    @property
    def nvr_name(self):
        """
        Return the RPM name.

        Returns:
            str: The name of the Build.
        """
        return self._get_n_v_r()[0]

    @property
    def nvr_version(self):
        """
        Return the RPM version.

        Returns:
            str: The version of the Build.
        """
        return self._get_n_v_r()[1]

    @property
    def nvr_release(self):
        """
        Return the RPM release.

        Returns:
            str: The release of the Build.
        """
        return self._get_n_v_r()[2]

    def get_n_v_r(self):
        """
        Return the (name, version, release) of this build.

        Note: This does not directly return the Build's nvr attribute, which is a str.

        Returns:
            tuple: A 3-tuple representing the name, version and release from the build.
        """
        return (self.nvr_name, self.nvr_version, self.nvr_release)

    def get_tags(self, koji=None):
        """
        Return a list of koji tags for this build.

        Args:
            koji (bodhi.server.buildsys.Buildsysem or koji.ClientSession): A koji client. Defaults
                to calling bodhi.server.buildsys.get_session().
        Return:
            list: A list of strings of the Koji tags on this Build.
        """
        if not koji:
            koji = buildsys.get_session()
        return [tag['name'] for tag in koji.listTags(self.nvr)]

    def get_owner_name(self):
        """
        Return the koji username of the user who built the build.

        Returns:
            str: The username of the user.
        """
        return self._get_kojiinfo()['owner_name']

    def get_build_id(self):
        """
        Return the koji build id of the build.

        Returns:
            id: The task/build if of the build.
        """
        return self._get_kojiinfo()['id']

    def get_task_id(self) -> int:
        """
        Return the koji task id of the build.

        Returns:
            id: The task if of the build or None
        """
        return self._get_kojiinfo().get('task_id')

    def get_changelog(self, timelimit=0, lastupdate=False):
        """Will be overridden from child classes, when appropriate."""
        return ""

    def get_creation_time(self) -> datetime:
        """Return the creation time of the build."""
        return datetime.fromisoformat(self._get_kojiinfo()['creation_time'])

    def unpush(self, koji, from_side_tag=False):
        """
        Move this build back to the candidate tag and remove any pending tags.

        Args:
            koji (bodhi.server.buildsys.Buildsysem or koji.ClientSession): A koji client.
            from_side_tag (bool): if the build was originally built in a side-tag.
        """
        log.info('Unpushing %s' % self.nvr)
        release = self.update.release
        for tag in self.get_tags(koji):
            if tag == release.pending_signing_tag:
                log.info('Removing %s tag from %s' % (tag, self.nvr))
                koji.untagBuild(tag, self.nvr)
            if tag == release.pending_testing_tag:
                log.info('Removing %s tag from %s' % (tag, self.nvr))
                koji.untagBuild(tag, self.nvr)
            if tag == release.pending_stable_tag:
                log.info('Removing %s tag from %s' % (tag, self.nvr))
                koji.untagBuild(tag, self.nvr)
            if tag == release.testing_tag:
                if not from_side_tag:
                    log.info(f'Moving {self.nvr} from {tag} to {release.candidate_tag}')
                    koji.moveBuild(tag, release.candidate_tag, self.nvr)
                else:
                    log.info(f'Removing {tag} tag from {self.nvr}')
                    koji.untagBuild(tag, self.nvr)
            elif from_side_tag and tag == release.candidate_tag:
                log.info(f'Removing {tag} tag from {self.nvr}')
                koji.untagBuild(tag, self.nvr)

    def is_latest(self) -> bool:
        """Check if this is the latest build available in the stable tag."""
        koji_session = buildsys.get_session()
        # Get the latest builds in koji in a tag for a package
        koji_builds = koji_session.getLatestBuilds(
            self.update.release.stable_tag,
            package=self.package.name
        )

        for koji_build in koji_builds:
            build_creation_time = datetime.fromisoformat(koji_build['creation_time'])
            if self.get_creation_time() < build_creation_time:
                return False
        return True

    def update_test_cases(self, db):
        """
        Update the list of test cases for this build from the wiki.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
        Raises:
            ExternalCallException: When retrieving testcases from Wiki failed.
        """
        if not config.get('query_wiki_test_cases'):
            return

        start = datetime.now(timezone.utc)
        log.debug(f'Querying the wiki for test cases of {self.nvr}')
        try:
            wiki = MediaWiki(config.get('wiki_url'),
                             user_agent=config.get('wiki_user_agent'))
        except Exception as ex:
            raise ExternalCallException(f'Failed to connect to Fedora Wiki: {ex}')
        cat_page = f'Package {self.package.external_name} test cases'

        def list_categorymembers(wiki, cat_page, limit=500):
            try:
                response = wiki.categorymembers(cat_page, results=limit, subcategories=True)
            except Exception as ex:
                raise ExternalCallException(f'Failed retrieving testcases from Wiki: {ex}')
            members = [entry for entry in response[0] if entry != '']

            # Determine whether we need to recurse
            if len(response[1]) > 0 and len(members) < limit:
                for subcat in response[1]:
                    members.extend(list_categorymembers(wiki, subcat, limit=limit - len(members)))

            log.debug(f'Found the following testcases: {members}')
            return members

        fetched = set(list_categorymembers(wiki, cat_page))

        # Delete removed testcases
        for case in self.testcases:
            if case.name not in fetched:
                self.testcases.remove(case)
                log.debug(f'Removed testcase "{case.name}" from {self.nvr}')

        # Add new testcases
        for test in fetched:
            case = TestCase.get(test)
            if not case:
                case = TestCase(name=test)
                db.add(case)
                db.flush()
                log.debug(f'Found new testcase "{case.name}" and added to database')
            if case not in self.testcases:
                self.testcases.append(case)
                log.debug(f'Added testcase "{case.name}" to {self.nvr}')

        db.flush()
        log.debug(f'Finished querying for test cases in {datetime.now(timezone.utc) - start}')


class ContainerBuild(Build):
    """
    Represents a Container build.

    Note that this model uses single-table inheritance with its Build superclass.
    """

    __mapper_args__ = {
        'polymorphic_identity': ContentType.container,
    }


class FlatpakBuild(Build):
    """
    Represents a Flatpak build.

    Note that this model uses single-table inheritance with its Build superclass.
    """

    __mapper_args__ = {
        'polymorphic_identity': ContentType.flatpak,
    }


class ModuleBuild(Build):
    """
    Represents a Module build.

    Note that this model uses single-table inheritance with its Build superclass.

    Attributes:
        nvr (str): A unique Koji identifier for the module build.
    """

    __mapper_args__ = {
        'polymorphic_identity': ContentType.module,
    }

    @property
    def nvr_name(self):
        """
        Return the ModuleBuild's name.

        Returns:
            str: The name of the module.
        """
        return self._get_kojiinfo()['name']

    @property
    def nvr_version(self):
        """
        Return the the ModuleBuild's stream.

        Returns:
            str: The stream of the ModuleBuild.
        """
        return self._get_kojiinfo()['version']

    @property
    def nvr_release(self):
        """
        Return the ModuleBuild's version and context.

        Returns:
            str: The version of the ModuleBuild.
        """
        return self._get_kojiinfo()['release']


class RpmBuild(Build):
    """
    Represents an RPM build.

    Note that this model uses single-table inheritance with its Build superclass.

    Attributes:
        nvr (str): A dash (-) separated string of an RPM's name, version, and release (e.g.
            'bodhi-2.5.0-1.fc26')
        epoch (int): The RPM's epoch.
    """

    epoch = Column(Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': ContentType.rpm,
    }

    @property
    def evr(self):
        """
        Return the RpmBuild's epoch, version, release, all strings in a 3-tuple.

        Return:
            tuple: (epoch, version, release)
        """
        if not self.epoch:
            self.epoch = self._get_kojiinfo()['epoch']
            if not self.epoch:
                self.epoch = 0
        return (str(self.epoch), str(self.nvr_version), str(self.nvr_release))

    def get_latest(self):
        """
        Return the nvr string of the most recent evr that is less than this RpmBuild's nvr.

        If there is no other Build, this returns ``None``.

        Returns:
            str or None: An nvr string, formatted like RpmBuild.nvr. If there is no other
                Build, returns ``None``.
        """
        koji_session = buildsys.get_session()

        # Grab a list of builds tagged with ``Release.stable_tag`` release
        # tags, and find the most recent update for this package, other than
        # this one.  If nothing is tagged for -updates, then grab the first
        # thing in ``Release.dist_tag``.  We aren't checking
        # ``Release.candidate_tag`` first, because there could potentially be
        # packages that never make their way over stable, so we don't want to
        # generate ChangeLogs against those.
        latest = None
        evr = self.evr
        for tag in [self.release.stable_tag, self.release.dist_tag]:
            builds = koji_session.listTagged(
                tag, package=self.package.name, inherit=True)

            # Find the first build that is older than us
            for build in builds:
                old_evr = build_evr(build)
                if rpm.labelCompare(evr, old_evr) > 0:
                    latest = build['nvr']
                    break
            if latest:
                break
        return latest

    def get_changelog(self, timelimit=0, lastupdate=False):
        """
        Retrieve the RPM changelog of this package since it's last update, or since timelimit.

        Args:
            timelimit (int): Timestamp, specified as the number of seconds since 1970-01-01 00:00:00
                UTC.
            lastupdate (bool): Only returns changelog since last update.
        Return:
            str: The RpmBuild's changelog.
        """
        rpm_header = get_rpm_header(self.nvr)
        descrip = rpm_header['changelogtext']
        if not descrip:
            return ""

        who = rpm_header['changelogname']
        when = rpm_header['changelogtime']

        num = len(descrip)
        if not isinstance(when, list):
            when = [when]

        if lastupdate:
            lastpkg = self.get_latest()
            if lastpkg is not None:
                oldh = get_rpm_header(lastpkg)
                if oldh['changelogtext']:
                    timelimit = oldh['changelogtime']
                    if isinstance(timelimit, list):
                        timelimit = timelimit[0]

        str = ""
        i = 0
        while (i < num) and (when[i] > timelimit):
            try:
                str += '* %s %s\n%s\n' % (time.strftime("%a %b %e %Y",
                                          time.localtime(when[i])), who[i],
                                          descrip[i])
            except Exception:
                log.exception('Unable to add changelog entry for header %s',
                              rpm_header)
            i += 1
        return str


if parse_version(sqlalchemy_version) >= parse_version("1.4.0"):
    overlaps_kw = {"overlaps": "release"}
else:
    overlaps_kw = {}


class Update(Base):
    """
    This model represents an update.

    The update contains not just one package, but a collection of packages. Each
    package can be referenced only once in one Update. Packages are referenced
    through their Build objects using field ``builds`` below.

    Attributes:
        autokarma (bool): A boolean that indicates whether or not the update will
            be automatically pushed when the stable_karma threshold is reached.
        autotime (bool): A boolean that indicates whether or not the update will
            be automatically pushed when the time threshold is reached.
        stable_karma (int): A positive integer that indicates the amount of "good"
            karma the update must receive before being automatically marked as stable.
        stable_days (int): A positive integer that indicates the number of days an update
            needs to spend in testing before being automatically marked as stable.
        unstable_karma (int): A positive integer that indicates the amount of "bad"
            karma the update must receive before being automatically marked as unstable.
        require_bugs (bool): Indicates whether or not positive feedback needs to be
            provided for the associated bugs before the update can be considered
            stable.
        require_testcases (bool): Indicates whether or not the update requires that
            positive feedback be given on all associated wiki test cases before the
            update can pass to stable. If the update has no associated wiki test cases,
            this option has no effect.
        display_name (str): Allows the user to customize the name of the update.
        notes (str): Notes about the update. This is a human-readable field that
            describes what the update is for (e.g. the bugs it fixes).
        type (EnumSymbol): The type of the update (e.g. enhancement, bugfix, etc). It
            must be one of the values defined in :class:`UpdateType`.
        status (EnumSymbol): The current status of the update. Possible values include
            'pending' to indicate it is not yet in a repository, 'testing' to indicate it
            is in the testing repository, etc. It must be one of the values defined in
            :class:`UpdateStatus`.
        request (EnumSymbol): The requested status of the update. This must be one of the
            values defined in :class:`UpdateRequest` or ``None``.
        severity (EnumSymbol): The update's severity. This must be one of the values defined
            in :class:`UpdateSeverity`.
        suggest (EnumSymbol): Suggested action a user should take after applying the update.
            This must be one of the values defined in :class:`UpdateSuggestion`.
        locked (bool): Indicates whether or not the update is locked and un-editable.
            This is usually set by the composer because the update is going through a state
            transition.
        pushed (bool): Indicates whether or not the update has been pushed to its requested
            repository.
        critpath (bool): Indicates whether or not the update is for a "critical path"
            :class:`Package`. Critical path packages are packages that are required for
            basic functionality. For example, the kernel :class:`RpmPackage` is a critical
            path package.
        critpath_groups (str): Space-separated list of critical path groups the package(s)
            in this update are members of. More detailed version of critpath. Empty string
            means "no groups" (same as critpath=False); None/null means "feature not supported"
            (i.e. the configured critpath.type doesn't give grouped critpath info).
        close_bugs (bool): Indicates whether the Bugzilla bugs that this update is related
            to should be closed automatically when the update is pushed to stable.
        date_submitted (DateTime): The date that the update was created.
        date_modified (DateTime): The date the update was last modified or ``None``.
        date_approved (DateTime): The date the update was approved or ``None``.
        date_testing (DateTime): The date the update was placed into the testing repository
            or ``None``.
        date_stable (DateTime): The date the update was placed into the stable repository or
            ``None``.
        alias (str): The update alias (e.g. FEDORA-EPEL-2009-12345).
        release_id (int): A foreign key to the releases ``id``.
        release (Release): The ``Release`` object this update relates to via the ``release_id``.
        comments (sqlalchemy.orm.collections.InstrumentedList): A list of the :class:`Comment`
            objects for this update.
        builds (sqlalchemy.orm.collections.InstrumentedList): A list of :class:`Build` objects
            contained in this update.
        bugs (sqlalchemy.orm.collections.InstrumentedList): A list of :class:`Bug` objects
            associated with this update.
        user_id (int): A foreign key to the :class:`User` that created this update.
        test_gating_status (EnumSymbol): The test gating status of the update. This must be one
            of the values defined in :class:`TestGatingStatus` or ``None``. None indicates that
            Greenwave integration was not enabled when the update was created.
        compose (Compose): The :class:`Compose` that this update is currently being composed in. The
            update is locked if this is defined.
        from_tag (str): The koji tag from which the list of builds was
            originally populated (if any).
    """

    __tablename__ = 'updates'
    __exclude_columns__ = ('id', 'user_id', 'release_id', 'compose')
    __include_extras__ = ('date_pushed', 'meets_testing_requirements', 'url', 'title',
                          'version_hash')
    __get_by__ = ('alias',)

    autokarma = Column(Boolean, default=True, nullable=False)
    autotime = Column(Boolean, default=True, nullable=False)
    stable_karma = Column(Integer, nullable=False)
    stable_days = Column(Integer, nullable=False, default=0)
    unstable_karma = Column(Integer, nullable=False)
    require_bugs = Column(Boolean, default=False)
    require_testcases = Column(Boolean, default=False)

    display_name = Column(UnicodeText, nullable=False, default='')
    notes = Column(UnicodeText, nullable=False)  # Mandatory notes

    # Enumerated types
    type = Column(UpdateType.db_type(), nullable=False)
    status = Column(UpdateStatus.db_type(),
                    default=UpdateStatus.pending,
                    nullable=False, index=True)
    request = Column(UpdateRequest.db_type(), index=True)
    severity = Column(UpdateSeverity.db_type(), default=UpdateSeverity.unspecified)
    suggest = Column(UpdateSuggestion.db_type(), default=UpdateSuggestion.unspecified)

    # Flags
    locked = Column(Boolean, default=False)
    pushed = Column(Boolean, default=False)
    critpath = Column(Boolean, default=False)
    critpath_groups = Column(UnicodeText, nullable=True)

    # Bug settings
    close_bugs = Column(Boolean, default=True)

    # Timestamps
    date_submitted = Column(TZDateTime, default=partial(datetime.now, tz=timezone.utc), index=True)
    date_modified = Column(TZDateTime)
    date_approved = Column(TZDateTime)
    date_testing = Column(TZDateTime)
    date_stable = Column(TZDateTime)

    # eg: FEDORA-EPEL-2009-12345
    alias = Column(Unicode(64), unique=True, nullable=False)

    # Many-to-one relationships
    release_id = Column(Integer, ForeignKey('releases.id'), nullable=False)
    release = relationship('Release', lazy='joined', innerjoin=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='updates')

    # If the update is locked and a Compose exists for the same release and request, this will be
    # set to that Compose.
    compose = relationship(
        'Compose',
        primaryjoin=("and_(foreign(Update.release_id)==Compose.release_id, "
                     "foreign(Update.request)==Compose.request, "
                     "Update.locked==True)"),
        overlaps='release', back_populates='updates')

    # One-to-many relationships
    comments = relationship('Comment', back_populates='update', cascade="all,delete,delete-orphan",
                            order_by='Comment.timestamp', lazy='joined')

    builds = relationship('Build', back_populates='update', order_by='Build.nvr', lazy='joined')

    # Many-to-many relationships
    bugs = relationship('Bug', secondary=update_bug_table, back_populates='updates',
                        order_by='Bug.bug_id')

    # Greenwave
    test_gating_status = Column(TestGatingStatus.db_type(), default=None, nullable=True)

    # Koji tag, if any, from which the list of builds was populated initially.
    from_tag = Column(UnicodeText, nullable=True)

    def __init__(self, *args, **kwargs):
        """
        Initialize the Update.

        We use this as a way to inject an alias into the Update, since it is a required field and
        we don't want callers to have to generate the alias themselves.
        """
        # Let's give this Update an alias so the DB doesn't become displeased with us.
        if 'release' not in kwargs:
            raise ValueError('You must specify a Release when creating an Update.')
        prefix = kwargs['release'].id_prefix
        year = time.localtime()[0]
        id = hashlib.sha1(str(uuid.uuid4()).encode('utf-8')).hexdigest()[:10]
        alias = '%s-%s-%s' % (prefix, year, id)
        self.alias = alias
        self.release_id = kwargs['release'].id
        # we need this to be set for message publishing to work
        self.status = kwargs.get('status', UpdateStatus.pending)

        super(Update, self).__init__(*args, **kwargs)

        log.debug('Set alias for %s to %s' % (self.get_title(), alias))

        self._ready_for_testing(self, None)

    @property
    def version_hash(self):
        """
        Return a SHA1 hash of the Builds NVRs.

        Returns:
            str: a SHA1 hash of the builds NVRs.
        """
        nvrs = [x.nvr for x in self.builds]
        builds = " ".join(sorted(nvrs))
        return hashlib.sha1(str(builds).encode('utf-8')).hexdigest()

    # WARNING: consumers/composer.py assumes that this validation is performed!
    @validates('builds', include_backrefs=True)
    def validate_builds(self, key, build):
        """
        Validate builds being appended to ensure they are all the same type.

        Args:
            key (str): The field's key, which is un-used in this validator.
            build (Build): The build object which was appended to the list
                of builds.

        Raises:
            ValueError: If the build being appended is not the same type as the
                existing builds.
        """
        if not all(isinstance(b, type(build)) for b in self.builds):
            raise ValueError('An update must contain builds of the same type.')
        return build

    @validates('release', include_backrefs=True)
    def validate_release(self, key, release):
        """
        Make sure the release is the same content type as this update.

        Args:
            key (str): The field's key, which is un-used in this validator.
            release (Release): The release object which is being associated with this update.
        Raises:
            ValueError: If the release being associated is not the same content type as the
                update.
        """
        if release and self.content_type is not None:
            u = Update.query.filter(Update.release_id == release.id, Update.id != self.id).first()
            if u and u.content_type and u.content_type != self.content_type:
                raise ValueError('A release must contain updates of the same type.')
        return release

    @property
    def date_locked(self):
        """
        Return the time that this update became locked.

        Returns:
            datetime.datetime or None: The time this update became locked, or None if it is not
                locked.
        """
        if self.locked and self.compose is not None:
            return self.compose.date_created

    @hybrid_property
    def date_pushed(self):
        """
        Return the time that this update was pushed in repository.

        Returns:
            datetime.datetime or None: The most recent between date_testing and date_stable, or
                None if the update was never pushed in any repo.
        """
        if self.date_stable:
            return self.date_stable
        elif self.date_testing:
            return self.date_testing
        else:
            return None

    @property
    def mandatory_days_in_testing(self):
        """
        Calculate and return how many days an update should be in testing before becoming stable.

        :return: The number of mandatory days in testing.
        :rtype:  int
        """
        if self.critpath:
            return self.release.critpath_mandatory_days_in_testing
        else:
            return self.release.mandatory_days_in_testing

    @property
    def karma(self):
        """
        Calculate and return the karma for the Update.

        :return: The Update's current karma.
        :rtype:  int
        """
        positive_karma, negative_karma = self._composite_karma
        return positive_karma + negative_karma

    @property
    def _composite_karma(self):
        """
        Calculate and return a 2-tuple of the positive and negative karma.

        Sums the positive karma comments, and then sums the negative karma comments. The total karma
        is simply the sum of the two elements of this 2-tuple.

        Returns:
            tuple: A 2-tuple of (positive_karma, negative_karma).
        """
        positive_karma = 0
        negative_karma = 0
        users_counted = set()
        for comment in self.comments_since_karma_reset:
            if comment.karma and comment.user.name not in users_counted:
                # Make sure we only count the last comment this user made
                users_counted.add(comment.user.name)
                if comment.karma > 0:
                    positive_karma += comment.karma
                else:
                    negative_karma += comment.karma

        return positive_karma, negative_karma

    @property
    def comments_since_karma_reset(self):
        """
        Generate the comments since the most recent karma reset event.

        Karma is reset when :class:`Builds <Build>` are added or removed from an update.

        Returns:
            list: class:`Comments <Comment>` since the karma reset.
        """
        # We want to traverse the comments in reverse order so we only consider
        # the most recent comments from any given user and only the comments
        # since the most recent karma reset event.
        comments_since_karma_reset = []

        for comment in reversed(self.comments):
            if comment.user.name == 'bodhi' and \
                    ('New build' in comment.text or 'Removed build' in comment.text):
                # We only want to consider comments since the most recent karma
                # reset, which happens whenever a build is added or removed
                # from an Update. Since we are traversing the comments in
                # reverse order, once we find one of these comments we can
                # simply exit this loop.
                break
            comments_since_karma_reset.append(comment)

        return comments_since_karma_reset

    @staticmethod
    def get_critpath_groups(builds, release_branch):
        """
        Determine which (if any) critpath groups the builds passed in are part of.

        Args:
            builds (list): :class:`Builds <Build>` to be considered.
            release_branch (str): The name of the git branch associated to the release,
                such as "f25" or "master".
        Returns:
            str: A space-separated list of the critpath groups. Will be empty if none.
        Raises:
            ValueError: If the configured critpath.type does not list by group.
        """
        components = build_names_by_type(builds)
        groups = []

        for ptype in components:
            groups.extend(
                get_grouped_critpath_components(
                    release_branch, ptype, frozenset(components[ptype])
                )
            )
        return " ".join(groups)

    @staticmethod
    def contains_critpath_component(builds, release_branch):
        """
        Determine if there is a critpath component in the builds passed in.

        Args:
            builds (list): :class:`Builds <Build>` to be considered.
            release_branch (str): The name of the git branch associated to the release,
                such as "f25" or "master".
        Returns:
            bool: ``True`` if the update contains a critical path package, ``False`` otherwise.
        """
        components = build_names_by_type(builds)

        for ptype in components:
            if get_critpath_components(release_branch, ptype, frozenset(components[ptype])):
                return True

        return False

    @property
    def greenwave_subject(self):
        """
        Form and return the proper Greenwave API subject field for this Update.

        Returns:
            list: A list of dictionaries that are appropriate to be passed to the Greenwave API
                subject field for a decision about this Update.
        """
        # See discussion on https://pagure.io/greenwave/issue/34 for why we use these subjects.
        subject = [{'item': build.nvr, 'type': 'koji_build'} for build in self.builds]
        subject.append({'item': self.alias, 'type': 'bodhi_update'})
        return subject

    def greenwave_request_batches(self, verbose):
        """
        Form and return the proper Greenwave API requests data for this Update.

        Returns:
            list: A list of dictionaries that are appropriate to be passed to the Greenwave API
                for a decision about this Update.
        """
        batch_size = self.greenwave_subject_batch_size
        count = 0
        subjects = self.greenwave_subject
        data = []
        while count < len(subjects):
            data.append({
                'product_version': self.product_version,
                'decision_context': self._greenwave_decision_contexts,
                'subject': subjects[count:count + batch_size],
                'verbose': verbose,
            })
            count += batch_size
        return data

    @property
    def greenwave_request_batches_json(self):
        """
        Form and return the proper Greenwave API requests data for this Update as JSON.

        Returns:
            str: A JSON list of objects that are appropriate to be passed to the Greenwave
                API for a decision about this Update.
        """
        return json.dumps(self.greenwave_request_batches(verbose=True))

    @property
    def greenwave_subject_batch_size(self):
        """Maximum number of subjects in single Greenwave request."""
        return config.get('greenwave_batch_size', 8)

    @property
    def _greenwave_api_url(self):
        if not config.get('greenwave_api_url'):
            raise BodhiException('No greenwave_api_url specified')

        return '{}/decision'.format(config.get('greenwave_api_url'))

    @property
    def _greenwave_decision_contexts(self):
        """
        Return greenwave contexts that should be queried for this update.

        The base context depends whether the update is going to
        testing (status=pending) or to stable (status=testing). We
        also query on additional contexts for critpath updates. If the
        critpath type provides grouped information, we query on one
        additional context per critpath group represented in the
        update's packages. If it does not, we query on the catch-all
        additional 'critpath' context.
        """
        # this is correct if update is already in testing...
        contexts = ["bodhi_update_push_stable"]
        if self.request == UpdateRequest.testing and self.status == UpdateStatus.pending:
            # ...but if it is pending, we want to know if it can go to testing
            contexts = ["bodhi_update_push_testing"]
        if self.critpath_groups:
            ocontext = contexts[0]
            for group in self.critpath_groups.split(" "):
                contexts.insert(0, f"{ocontext}_{group}_critpath")
        elif self.critpath:
            contexts.insert(0, contexts[0] + "_critpath")
        return contexts

    def get_test_gating_info(self):
        """
        Query Greenwave about this update and return the information retrieved.

        Returns:
            list: A list of response dicts from Greenwave for this update.
        Raises:
            BodhiException: When the ``greenwave_api_url`` is undefined in configuration.
            RuntimeError: If Greenwave did not give us a 200 code.
        """
        return [util.greenwave_api_post(self._greenwave_api_url, data)
                for data in self.greenwave_request_batches(verbose=True)]

    @property
    def _greenwave_requirements_generator(self):
        """
        Query Greenwave about this update and return satisfied and unsatisfied requirements.

        Returns:
            generator: An iterable of 2-tuples of lists of requirement dicts from each request
            batch: first tuple item satisfied requirements, second item unsatisfied requirements.
            Either list or both may be empty.

        Raises:
            BodhiException: When the ``greenwave_api_url`` is undefined in configuration.
            RuntimeError: If Greenwave did not give us a 200 code, including if no applicable
            policies were found.
        """
        for data in self.greenwave_request_batches(verbose=False):
            response = util.greenwave_api_post(self._greenwave_api_url, data)
            satisfied = response.get('satisfied_requirements', [])
            unsatisfied = response.get('unsatisfied_requirements', [])
            yield (satisfied, unsatisfied)

    @property
    def _unsatisfied_requirements(self):
        """Query Greenwave about this update and return all unsatisfied requirements.

        Returns:
            list: A list of unsatisfied requirement dicts.

        Raises:
            BodhiException: When the ``greenwave_api_url`` is undefined in configuration.
            RuntimeError: If Greenwave did not give us a 200 code, including if no applicable
            policies were found.
        """
        ret = []
        for (_, unsatisfied) in self._greenwave_requirements_generator:
            ret.extend(unsatisfied)
        return ret

    def _get_test_gating_status(self):
        """
        Query Greenwave about this update and return the information retrieved.

        Returns:
            TestGatingStatus:
                - TestGatingStatus.ignored if no tests are required
                - TestGatingStatus.passed if there are required tests and policies are satisfied
                - TestGatingStatus.waiting if there are required tests that have not yet completed,
                  no required test has failed, and update was last modified less than 2 hours ago
                - TestGatingStatus.failed otherwise (failed required tests, missing required
                  test results and last modified more than 2 hours ago)

        Raises:
            BodhiException: When the ``greenwave_api_url`` is undefined in configuration.
            RuntimeError: If Greenwave did not give us a 200 code, including if no applicable
            policies were found.
        """
        gotsat = False
        gotunsat = False
        recent = datetime.now(timezone.utc) - self.last_modified < timedelta(hours=2)
        for (satisfied, unsatisfied) in self._greenwave_requirements_generator:
            if satisfied:
                gotsat = True
            if unsatisfied:
                gotunsat = True
                if not all(req.get('type', '') == 'test-result-missing' for req in unsatisfied):
                    # some unsats must be failures
                    return TestGatingStatus.failed
                if not recent and not all(req.get('result_id') for req in unsatisfied):
                    # all unsats are missing, but it's more than two
                    # hours since the update was edited and we don't
                    # have QUEUED or RUNNING results for all of them
                    return TestGatingStatus.failed

        if not gotsat and not gotunsat:
            return TestGatingStatus.ignored

        if gotsat and not gotunsat:
            return TestGatingStatus.passed

        # here, we have unsatisfied requirements but we never bailed early
        # in the for loop, so they are all 'missing' and update was recently modified
        return TestGatingStatus.waiting

    @property
    def install_command(self) -> str:
        """
        Return the appropriate command for installing the Update.

        There are four conditions under which the empty string is returned:
            * If the update is in testing status for rawhide.
            * If the update is not in a stable or testing repository.
            * If the release has not specified a package manager.
            * If the release has not specified a testing repository.

        Returns:
            The dnf command to install the Update, or the empty string.
        """
        if not self.release.composed_by_bodhi and self.status == UpdateStatus.testing:
            return ''

        if self.status != UpdateStatus.stable and self.status != UpdateStatus.testing:
            return ''

        if self.release.package_manager == PackageManager.unspecified \
                or self.release.testing_repository is None:
            return ''

        command = 'sudo {} {}{}{} --advisory={}{}'.format(
            self.release.package_manager.value,
            'install' if self.type == UpdateType.newpackage else 'upgrade',
            (' --enablerepo=' + self.release.testing_repository)
            if self.status == UpdateStatus.testing else '',
            ' --refresh' if self.release.package_manager.value == 'dnf' else '',
            self.alias,
            r' \*' if self.type == UpdateType.newpackage else '')
        return command

    def update_test_gating_status(self):
        """Query Greenwave about this update and set the test_gating_status as appropriate."""
        try:
            self.test_gating_status = self._get_test_gating_status()
        except (requests.exceptions.Timeout, RuntimeError) as e:
            log.error(str(e))
            # If we receive a 500 error code from Greenwave, we set the test_gating_status to
            # waiting. The status will then be updated later by the greenwave fedora-messaging
            # consumer.
            self.test_gating_status = TestGatingStatus.waiting

    @classmethod
    def new(cls, request, data):
        """
        Create a new update.

        Args:
            request (pyramid.request.Request): The current web request.
            data (dict): A key-value mapping of the new update's attributes.
        Returns:
            tuple: A 2-tuple of the edited update and a list of dictionaries that describe caveats.
        """
        db = request.db
        user = User.get(request.identity.name)
        data['user'] = user
        caveats = []
        try:
            data['critpath_groups'] = cls.get_critpath_groups(
                data['builds'], data['release'].branch)
            data['critpath'] = bool(data['critpath_groups'])
        except ValueError:
            data['critpath_groups'] = None
            data['critpath'] = cls.contains_critpath_component(
                data['builds'], data['release'].branch)

        # Be sure to not add an empty string as alternative title
        # and strip whitespaces from it
        if 'display_name' in data:
            data['display_name'] = data['display_name'].strip()

        # Create the Bug entities, but don't talk to rhbz yet.  We do that
        # offline in the UpdatesHandler task worker now.
        bugs = []
        if data['bugs']:
            for bug_num in data['bugs']:
                bug = db.query(Bug).filter_by(bug_id=bug_num).first()
                if not bug:
                    bug = Bug(bug_id=bug_num)
                    db.add(bug)
                    db.flush()
                bugs.append(bug)
        data['bugs'] = bugs

        del data['edited']

        req = data.pop("request", UpdateRequest.testing)

        # Create the update
        log.debug("Creating new Update(**data) object.")
        release = data.pop('release', None)

        if not release.composed_by_bodhi:
            # For rawhide updates make sure autotime push is enabled
            # https://github.com/fedora-infra/bodhi/issues/3912
            data['autotime'] = True
            data['stable_days'] = 0
            log.debug("Overriding autotime settings for rawhide update.")

        up = Update(**data, release=release)

        # We want to make sure that the value of stable_days
        # will not be lower than the mandatory_days_in_testing.
        if up.mandatory_days_in_testing > up.stable_days:
            up.stable_days = up.mandatory_days_in_testing
            caveats.append({
                'name': 'stable days',
                'description': "The number of stable days required was set to the mandatory "
                               f"release value of {up.mandatory_days_in_testing} days"
            })

        # We also need to make sure stable_karma is not set below
        # the policy minimum for this release
        if release.min_karma > up.stable_karma:
            up.stable_karma = release.min_karma
            caveats.append({
                'name': 'stable karma',
                'description': "The stable karma required was set to the mandatory "
                               f"release value of {release.min_karma}"
            })

        log.debug(f"Adding new update to the db {up.alias}.")
        db.add(up)
        log.debug(f"Triggering db commit for new update {up.alias}.")
        db.commit()

        log.info("Deferring working on bugs and fetching test cases to celery")
        alias = up.alias
        if not bool(config.get('bodhi_email')):
            log.warning("Not configured to handle bugs")
        else:
            bug_ids = [bug.bug_id for bug in up.bugs]
            work_on_bugs_task.delay(alias, bug_ids)

        fetch_test_cases_task.delay(alias)

        # track whether to set gating status shortly...
        setgs = config.get('test_gating.required')
        # The request to testing for side-tag updates is set within the signed consumer
        if not data.get("from_tag"):
            log.debug(f"Setting request for new update {up.alias}.")
            up.set_request(db, req, request.identity.name)
            if req == UpdateRequest.testing:
                # set_request will update gating status if necessary
                setgs = False

        if setgs:
            log.debug(
                'Test gating required is enforced, marking the update as waiting on test gating')
            up.test_gating_status = TestGatingStatus.waiting

        log.debug(f"Done with Update.new(...) {up.alias}")
        return up, caveats

    @classmethod
    def edit(cls, request, data):
        """
        Edit the update.

        Args:
            request (pyramid.request.Request): The current web request.
            data (dict): A key-value mapping of what should be altered in this update.
        Returns:
            tuple: A 2-tuple of the edited update and a list of dictionaries that describe caveats.
        Raises:
            LockedUpdateException: If the update is locked.
        """
        db = request.db
        buildinfo = request.buildinfo
        up = db.query(Update).filter_by(alias=data['edited']).first()
        del data['edited']

        caveats = []
        edited_builds = [build.nvr for build in up.builds]

        # Be sure to not add an empty string as alternative title
        # and strip whitespaces from it
        if 'display_name' in data:
            data['display_name'] = data['display_name'].strip()

        # stable_days can be set by the user. We want to make sure that the value
        # will not be lower than the mandatory_days_in_testing.
        if up.mandatory_days_in_testing > data.get('stable_days', up.stable_days):
            data['stable_days'] = up.mandatory_days_in_testing
            caveats.append({
                'name': 'stable days',
                'description': "The number of stable days required was raised to the mandatory "
                               f"release value of {up.mandatory_days_in_testing} days"
            })

        # We also need to make sure stable_karma is not set below
        # the policy minimum for this release
        if up.release.min_karma > data.get('stable_karma', up.stable_karma):
            data['stable_karma'] = up.release.min_karma
            caveats.append({
                'name': 'stable karma',
                'description': "The stable karma required was raised to the mandatory "
                               f"release value of {up.release.min_karma}"
            })

        # Determine which builds have been added
        new_builds = []
        for build in data['builds']:
            if build not in edited_builds:
                if up.locked:
                    raise LockedUpdateException("Can't add builds to a "
                                                "locked update")

                new_builds.append(build)
                Package.get_or_create(db, buildinfo[build])
                b = db.query(Build).filter_by(nvr=build).first()

                up.builds.append(b)

        # Determine which builds have been removed
        removed_builds = []
        for build in edited_builds:
            if build not in data['builds']:
                if up.locked:
                    raise LockedUpdateException("Can't remove builds from a "
                                                "locked update")

                removed_builds.append(build)
                b = None
                for b in up.builds:
                    if b.nvr == build:
                        break

                b.unpush(koji=request.koji, from_side_tag=bool(up.from_tag))
                up.builds.remove(b)

                # Expire any associated buildroot override
                if b.override:
                    log.debug(f"Expiring BRO for {b.nvr} because the build is unpushed.")
                    b.override.expire()
                else:
                    # Only delete the Build entity if it isn't associated with
                    # an override
                    db.delete(b)

        try:
            data['critpath_groups'] = cls.get_critpath_groups(
                up.builds, up.release.branch)
            data['critpath'] = bool(data['critpath_groups'])
        except ValueError:
            data['critpath_groups'] = None
            data['critpath'] = cls.contains_critpath_component(
                up.builds, up.release.branch)

        del data['builds']

        # Comment on the update with details of added/removed builds
        # .. enumerate the builds in markdown format so they're pretty.
        comment = '%s edited this update.' % request.identity.name
        if new_builds:
            comment += '\n\nNew build(s):\n'
            for new_build in new_builds:
                comment += "\n- %s" % new_build
        if removed_builds:
            comment += '\n\nRemoved build(s):\n'
            for removed_build in removed_builds:
                comment += "\n- %s" % removed_build
        if new_builds or removed_builds:
            comment += '\n\nKarma has been reset.'
        up.comment(db, comment, karma=0, author='bodhi')
        caveats.append({'name': 'builds', 'description': comment})

        # Updates with new or removed builds always go back to testing
        if new_builds or removed_builds:
            data['request'] = UpdateRequest.testing
            up.date_testing = None

            if (
                (up.status != UpdateStatus.pending and not up.from_tag)
                or (up.status != UpdateStatus.pending and up.from_tag
                    and up.release.composed_by_bodhi)
            ):
                # Remove all koji tags and change the status back to pending
                up.unpush(db)
                caveats.append({
                    'name': 'status',
                    'description': 'Builds changed.  Your update is being '
                    'sent back to testing.',
                })
                builds_to_tag = [b.nvr for b in up.builds]
            else:
                # No need to unpush the update, just tag new builds
                # into the appropriate pending-signing tag
                # and release-candidate tag if builds are in side-tag
                builds_to_tag = new_builds

            tags = []
            if up.from_tag and not up.release.composed_by_bodhi:
                tags.append(up.release.get_pending_signing_side_tag(up.from_tag))
            elif up.from_tag:
                tags.append(up.release.candidate_tag)
                if up.release.pending_signing_tag:
                    tags.append(up.release.pending_signing_tag)
            else:
                # For normal updates the builds already have candidate_tag
                if up.release.pending_signing_tag:
                    tags.append(up.release.pending_signing_tag)

            for tag in tags:
                tag_update_builds_task.delay(tag=tag, builds=builds_to_tag)

        new_bugs = up.update_bugs(data['bugs'], db)
        del data['bugs']

        req = data.pop("request", None)
        if req is not None and up.release.composed_by_bodhi:
            up.set_request(db, req, request.identity.name)

        for key, value in data.items():
            setattr(up, key, value)

        up.date_modified = datetime.now(timezone.utc)

        notifications.publish(update_schemas.UpdateEditV2.from_dict(
            message={
                'update': up,
                'agent': request.identity.name,
                'new_bugs': new_bugs,
                'new_builds': new_builds,
                'removed_builds': removed_builds
            }
        ))
        if (new_builds or removed_builds) and up.content_type == ContentType.rpm:
            message = update_schemas.UpdateReadyForTestingV3.from_dict(
                message=up._build_group_test_message(agent=request.identity.name)
            )
            notifications.publish(message)

        # If editing a Pending update, all of whose builds are signed, for a release
        # which isn't composed by Bodhi (i.e. Rawhide), move it directly to Testing.
        if not up.release.composed_by_bodhi and up.status == UpdateStatus.pending \
                and up.signed:
            log.info("Every build in the update is signed, set status to testing")
            up.status = UpdateStatus.testing
            up.date_testing = func.current_timestamp()
            up.request = None
            log.info(f"Update status of {up.alias} has been set to testing")

        if config['test_gating.required']:
            log.info(f"Updating test gating status of {up.alias}")
            up.update_test_gating_status()

        # Commit the changes in the db before calling celery tasks.
        db.commit()

        log.info("Deferring working on bugs and fetching test cases to celery")
        alias = up.alias
        if not bool(config.get('bodhi_email')):
            log.warning("Not configured to handle bugs")
        else:
            work_on_bugs_task.delay(alias, new_bugs)

        fetch_test_cases_task.delay(alias)

        log.info(f"Done editing {up.alias}")
        return up, caveats

    @property
    def signed(self):
        """
        Return whether the update is considered signed or not.

        This will return ``True`` if all :class:`Builds <Build>` associated with this update are
        signed, or if the associated :class:`Release` does not have a ``pending_signing_tag``
        defined. Otherwise, it will return ``False``.

        If the update is created ``from_tag`` always check if every build is signed.

        Returns:
            bool: ``True`` if the update is signed, ``False`` otherwise.
        """
        if not self.release.pending_signing_tag and not self.from_tag:
            return True
        return all(build.signed for build in self.builds)

    @property
    def content_type(self):
        """
        Return the ContentType associated with this update.

        If the update has no :class:`Builds <Build>`, this evaluates to ``None``.

        Returns:
            ContentType or None: The content type of this update or ``None``.
        """
        if self.builds:
            return self.builds[0].type

    @property
    def test_gating_passed(self) -> bool:
        """
        Returns a boolean representing if this update has passed the test gating.

        Returns:
            True if the Update's test_gating_status property is None,
            ignored, or passed. Otherwise it returns False.
        """
        if self.test_gating_status in (
                None, TestGatingStatus.ignored, TestGatingStatus.passed):
            return True
        return False

    def obsolete_older_updates(self, db):
        """Obsolete any older pending/testing updates.

        If a build is associated with multiple updates, make sure that
        all updates are safe to obsolete, or else just skip it.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
        Returns:
            list: A list of dictionaries that describe caveats.
        """
        caveats = []
        for build in self.builds:
            for oldBuild in db.query(Build).join(Update).filter(
                and_(Build.nvr != build.nvr,
                     Build.package == build.package,
                     Update.locked.is_(False),
                     Update.release == self.release,
                     or_(and_(or_(Update.status == UpdateStatus.testing,
                                  Update.status == UpdateStatus.pending),
                              or_(Update.request != UpdateRequest.stable,
                                  Update.request.is_(None))),
                         and_(or_(Update.status == UpdateStatus.testing,
                                  Update.status == UpdateStatus.pending),
                              Update.request == UpdateRequest.stable,
                              self.request == UpdateRequest.stable)))
            ).all():
                obsoletable = False
                nvr = build.get_n_v_r()
                if rpm.labelCompare(oldBuild.get_n_v_r(), nvr) < 0:
                    log.debug("%s is newer than %s" % (nvr, oldBuild.nvr))
                    obsoletable = True

                # Ensure that all of the packages in the old update are
                # present in the new one.
                pkgs = [b.package.name for b in self.builds]
                for _build in oldBuild.update.builds:
                    if _build.package.name not in pkgs:
                        obsoletable = False
                        break

                # Warn if you're stomping on another user but don't necessarily
                # obsolete them
                if len(oldBuild.update.builds) != len(self.builds):
                    if oldBuild.update.user.name != self.user.name:
                        caveats.append({
                            'name': 'update',
                            'description': 'Please be aware that there '
                            'is another update in flight owned by %s, '
                            'containing %s. Are you coordinating with '
                            'them?' % (
                                oldBuild.update.user.name,
                                oldBuild.nvr,
                            )
                        })

                # Warn about attempt to obsolete security update by update with
                # other type and set type of new update to security.
                if oldBuild.update.type == UpdateType.security and \
                        self.type is not UpdateType.security:
                    caveats.append({
                        'name': 'update',
                        'description': 'Adjusting type of this update to security,'
                        'since it obsoletes another security update'
                    })
                    self.type = UpdateType.security
                    self.severity = oldBuild.update.severity

                if obsoletable:
                    log.info('%s is obsoletable' % oldBuild.nvr)

                    # Have the newer update inherit the older updates bugs
                    oldbugs = [bug.bug_id for bug in oldBuild.update.bugs]
                    bugs = [bug.bug_id for bug in self.bugs]
                    self.update_bugs(bugs + oldbugs, db)

                    # Also inherit the older updates notes as well and
                    # add a markdown separator between the new and old ones.
                    # If it's an automatic update, do not copy the changelog again.
                    re_changelog = re.compile(r"(?s)\n##### \*\*Changelog\*\*\n\n```\n.*\n```")
                    old_notes = re.sub(re_changelog, '', oldBuild.update.notes)
                    new_notes = self.notes + '\n\n----\n\n' + old_notes
                    if len(new_notes) <= config.get('update_notes_maxlength'):
                        self.notes = new_notes
                    oldBuild.update.obsolete(db, newer=build)
                    template = ('This update has obsoleted %s, and has '
                                'inherited its bugs and notes.')
                    link = "[%s](%s)" % (oldBuild.nvr,
                                         oldBuild.update.abs_url())
                    self.comment(db, template % link, author='bodhi')
                    caveats.append({
                        'name': 'update',
                        'description': template % oldBuild.nvr,
                    })

        return caveats

    def get_tags(self):
        """
        Return all koji tags for all builds on this update.

        Returns:
            list: strings of the koji tags used in this update.
        """
        return list(set(sum([b.get_tags() for b in self.builds], [])))

    @property
    def title(self) -> str:
        """
        Return the Update's title.

        This is just an alias for get_title with default parameters.
        """
        return self.get_title()

    def get_title(self, delim=' ', limit=None, after_limit='…',
                  beautify=False, nvr=False, amp=False):
        """
        Return a title for the update based on the :class:`Builds <Build>` it is associated with.

        Args:
            delim (str): The delimiter used to separate the builds. Defaults to ' '.
            limit (int or None): If provided, limit the number of builds included to the given
                number. If ``None`` (the default), no limit is used.
            after_limit (str): If a limit is set, use this string after the limit is reached.
                Defaults to '…'.
            beautify (bool): If provided, the returned string will be human
                readable, i.e. 3 or more builds will take the form "package1,
                package2 and XXX more".
            nvr (bool): If specified, the title will include name, version and
                release information in package labels.
            amp (bool): If specified, it will replace the word 'and' with an
                ampersand, '&'.
        Returns:
            str: A title for this update.
        """
        if beautify:
            if self.display_name:
                return self.display_name

            def build_label(build):
                return build.nvr if nvr else build.package.name

            if len(self.builds) > 2:
                title = ", ".join([build_label(build) for build in self.builds[:2]])

                if amp:
                    title += ", & "
                else:
                    title += ", and "
                title += str(len(self.builds) - 2)
                title += " more"

                return title
            elif len(self.builds) == 0:
                return self.alias
            else:
                return " and ".join([build_label(build) for build in self.builds])
        else:
            if len(self.builds) == 0:
                return self.alias
            all_nvrs = [x.nvr for x in self.builds]
            nvrs = all_nvrs[:limit]
            builds = delim.join(sorted(nvrs)) + \
                (after_limit if limit and len(all_nvrs) > limit else "")
            return builds

    def get_bugstring(self, show_titles=False):
        """
        Return a space-delimited string of bug numbers for this update.

        Args:
            show_titles (bool): If True, include the bug titles in the output. If False, include
                only bug ids.
        Returns:
            str: A space separated list of bugs associated with this update.
        """
        val = ''
        if show_titles:
            bugstr = []
            for bug in self.bugs:
                bugstr.append(f"{bug.bug_id} - {bug.title}")
            val = '\n'.join(bugstr)
        else:
            val = ' '.join([str(bug.bug_id) for bug in self.bugs])
        return val

    def get_bug_karma(self, bug):
        """
        Return the karma for this update for the given bug.

        Args:
            bug (Bug): The bug we want the karma about.
        Returns:
            tuple: A 2-tuple of integers. The first represents negative karma, the second represents
            positive karma.
        """
        good, bad, seen = 0, 0, set()
        for comment in self.comments_since_karma_reset:
            if comment.user.name in seen:
                continue
            seen.add(comment.user.name)
            for feedback in comment.bug_feedback:
                if feedback.bug == bug:
                    if feedback.karma > 0:
                        good += 1
                    elif feedback.karma < 0:
                        bad += 1
        return bad * -1, good

    def get_testcase_karma(self, testcase):
        """
        Return the karma for this update for the given TestCase.

        Args:
            testcase (TestCase): The TestCase we want the karma about.
        Returns:
            tuple: A 2-tuple of integers. The first represents negative karma, the second represents
            positive karma.
        """
        good, bad, seen = 0, 0, set()
        for comment in self.comments_since_karma_reset:
            if comment.user.name in seen:
                continue
            seen.add(comment.user.name)
            for feedback in comment.unique_testcase_feedback:
                if feedback.testcase == testcase:
                    if feedback.karma > 0:
                        good += 1
                    elif feedback.karma < 0:
                        bad += 1
        return bad * -1, good

    def set_request(self, db, action, username):
        """
        Set the update's request to the given action.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
            action (UpdateRequest or str): The desired request. May be expressed as an
                UpdateRequest instance, or as a string describing the desired request.
            username (str): The username of the user making the request.
        Raises:
            BodhiException: Two circumstances can raise this ``Exception``:

                * If the user tries to push a critical path update directly from pending to stable.
                * If the update doesn't meet testing requirements.

            LockedUpdateException: If the update is locked.
        """
        log.debug('Attempting to set request %s' % action)
        notes = []
        if isinstance(action, str):
            action = UpdateRequest.from_string(action)
        if self.status and action.description == self.status.description:
            log.info("%s already %s" % (self.alias, action.description))
            return
        if action is self.request:
            log.debug("%s has already been submitted to %s" % (self.alias,
                                                               self.request.description))
            return

        if self.locked:
            raise LockedUpdateException("Can't change the request on a "
                                        "locked update")

        if not self.release.composed_by_bodhi \
                and action == (UpdateRequest.stable or UpdateRequest.testing):
            raise BodhiException('Setting a request on an Update for a Release '
                                 'not composed by Bodhi is not allowed')

        if action is UpdateRequest.unpush:
            self.unpush(db)
            self.comment(db, u'This update has been unpushed.', author=username)
            notifications.publish(update_schemas.UpdateRequestUnpushV1.from_dict(dict(
                update=self, agent=username)))
            log.debug("%s has been unpushed." % self.alias)
            return
        elif action is UpdateRequest.obsolete:
            self.obsolete(db)
            log.debug("%s has been obsoleted." % self.alias)
            notifications.publish(update_schemas.UpdateRequestObsoleteV1.from_dict(dict(
                update=self, agent=username)))
            return

        # If status is pending going to testing request and action is revoke,
        # set the status to unpushed
        elif self.status is UpdateStatus.pending and self.request is UpdateRequest.testing \
                and action is UpdateRequest.revoke:
            self.status = UpdateStatus.unpushed
            self.revoke()
            log.debug("%s has been revoked." % self.alias)
            notifications.publish(update_schemas.UpdateRequestRevokeV1.from_dict(dict(
                update=self, agent=username)))
            return

        # If status is testing going to stable request and action is revoke,
        # keep the status at testing
        elif self.request == UpdateRequest.stable and \
                self.status is UpdateStatus.testing and action is UpdateRequest.revoke:
            self.revoke()
            log.debug("%s has been revoked." % self.alias)
            notifications.publish(update_schemas.UpdateRequestRevokeV1.from_dict(dict(
                update=self, agent=username)))
            return

        elif action is UpdateRequest.revoke:
            self.revoke()
            log.debug("%s has been revoked." % self.alias)
            notifications.publish(update_schemas.UpdateRequestRevokeV1.from_dict(dict(
                update=self, agent=username)))
            return

        # Disable pushing updates from pending directly to stable when the release is frozen
        if (
            action == UpdateRequest.stable and self.status == UpdateStatus.pending
            and self.release.state == ReleaseState.frozen
        ):
            raise BodhiException(
                'The release of this update is frozen and the update has not yet been '
                'pushed to testing. It is currently not possible to push it to stable.')

        # Don't allow push to stable unless testing requirements are met
        if action == UpdateRequest.stable:
            met, reason = self.meets_requirements_why
            if not met:
                if self.release.id_prefix == "FEDORA-EPEL":
                    msg = config.get('not_yet_tested_epel_msg')
                else:
                    msg = config.get('not_yet_tested_msg')
                msg = f'{msg}: {reason}'
                notes.append(msg)

                if self.status is UpdateStatus.testing:
                    self.request = None
                    raise BodhiException('. '.join(notes))
                elif self.request is UpdateRequest.testing:
                    raise BodhiException('. '.join(notes))
                else:
                    log.info('Forcing update into testing')
                    action = UpdateRequest.testing

        # Add the appropriate 'pending' koji tag to this update, so tools
        # could compose repositories of them for testing.
        # If it's a new side-tag update, koji tags are managed by the celery task
        if action is UpdateRequest.testing and not self.from_tag:
            self.add_tag(self.release.pending_signing_tag)
            if self.release.candidate_tag not in self.get_tags():
                self.add_tag(self.release.candidate_tag)
        elif action is UpdateRequest.stable:
            self.add_tag(self.release.pending_stable_tag)
            if self.request == UpdateRequest.testing:
                self.remove_tag(self.release.pending_testing_tag)

        # If an obsolete/unpushed build is being re-submitted, return
        # it to the pending state, and make sure it's tagged as a candidate
        if self.status in (UpdateStatus.obsolete, UpdateStatus.unpushed):
            self.status = UpdateStatus.pending

        self.request = action

        notes = notes and '. '.join(notes) + '.' or ''
        log.debug(
            "%s has been submitted for %s. %s" % (
                self.alias, action.description, notes))

        comment_text = 'This update has been submitted for %s by %s. %s' % (
            action.description, username, notes)
        # Add information about push to stable delay to comment when release is frozen.
        if self.release.state == ReleaseState.frozen and action == UpdateRequest.stable:
            comment_text += (
                "\n\nThere is an ongoing freeze; this will be "
                "pushed to stable after the freeze is over. "
            )
        self.comment(db, comment_text, author=u'bodhi')

        action_message_map = {
            UpdateRequest.revoke: update_schemas.UpdateRequestRevokeV1,
            UpdateRequest.stable: update_schemas.UpdateRequestStableV1,
            UpdateRequest.testing: update_schemas.UpdateRequestTestingV1,
            UpdateRequest.unpush: update_schemas.UpdateRequestUnpushV1,
            UpdateRequest.obsolete: update_schemas.UpdateRequestObsoleteV1}
        notifications.publish(action_message_map[action].from_dict(
            dict(update=self, agent=username)))

        if action == UpdateRequest.testing:
            if config['test_gating.required']:
                log.info(f"Updating test gating status of {self.alias}")
                self.update_test_gating_status()

        if action == UpdateRequest.stable:
            self.obsolete_older_updates(db)

        # Commit the changes in the db before calling a celery task.
        db.commit()

    def waive_test_results(self, username, comment=None, tests=None):
        """
        Attempt to waive test results for this update.

        Args:
            username (str): The name of the user who is waiving the test results.
            comment (str): A comment from the user describing their decision.
            tests (list of str): A list of testcases to be waived. Defaults to ``None``
                If left as ``None``, all ``unsatisfied_requirements`` returned by greenwave
                will be waived, otherwise only the testcase found in both list will be waived.
        Raises:
            LockedUpdateException: If the Update is locked.
            BodhiException: If test gating is not enabled in this Bodhi instance,
                            or if the tests have passed.
            RuntimeError: Either WaiverDB or Greenwave did not give us a 200 code.
        """
        log.debug('Attempting to waive test results for this update %s' % self.alias)

        if self.locked:
            raise LockedUpdateException("Can't waive test results on a "
                                        "locked update")

        if not config.get('test_gating.required'):
            raise BodhiException('Test gating is not enabled')

        if self.test_gating_passed:
            raise BodhiException("Can't waive test results on an update that passes test gating")

        # Ensure we can always iterate over tests
        tests = tests or []

        for requirement in self._unsatisfied_requirements:

            if tests and requirement['testcase'] not in tests:
                continue

            data = {
                'subject_type': requirement['subject_type'],
                'subject_identifier': requirement['subject_identifier'],
                'testcase': requirement['testcase'],
                'scenario': requirement.get('scenario', None),
                'product_version': self.product_version,
                'waived': True,
                'username': username,
                'comment': comment
            }
            log.debug('Waiving test results: %s' % data)
            util.waiverdb_api_post(
                '{}/waivers/'.format(config.get('waiverdb_api_url')), data)

        self.test_gating_status = TestGatingStatus.waiting

    def add_tag(self, tag):
        """
        Add the given koji tag to all :class:`Builds <Build>` in this update.

        Args:
            tag (str): The tag to be added to the builds.
        """
        log.debug('Adding tag %s to %s', tag, self.get_title())
        if not tag:
            log.warning("Not adding builds of %s to empty tag", self.title)
            return []  # An empty iterator in place of koji multicall

        koji = buildsys.get_session()
        koji.multicall = True
        for build in self.builds:
            koji.tagBuild(tag, build.nvr, force=True)
        return koji.multiCall()

    def remove_tag(self, tag, koji=None):
        """
        Remove the given koji tag from all builds in this update.

        Args:
            tag (str): The tag to remove from the :class:`Builds <Build>` in this update.
            koji (koji.ClientSession or None): A koji client to use to perform the action. If None
                (the default), this method will use :func:`buildsys.get_session` to get one and
                multicall will be used.
        Returns:
            list or None: If a koji client was provided, ``None`` is returned. Else, a list of tasks
                from ``koji.multiCall()`` are returned.
        """
        log.debug('Removing tag %s from %s', tag, self.get_title())
        if not tag:
            log.warning("Not removing builds of %s from empty tag", self.get_title())
            return []  # An empty iterator in place of koji multicall

        return_multicall = not koji
        if not koji:
            koji = buildsys.get_session()
            koji.multicall = True
        for build in self.builds:
            koji.untagBuild(tag, build.nvr, force=True)
        if return_multicall:
            return koji.multiCall()

    def find_conflicting_builds(self) -> list:
        """
        Find if there are any builds conflicting with the stable tag in the update.

        Returns a list of conflicting builds, empty is none found.
        """
        conflicting_builds = []
        for build in self.builds:
            if not build.is_latest():
                conflicting_builds.append(build.nvr)

        return conflicting_builds

    def modify_bugs(self):
        """
        Comment on and close this update's bugs as necessary.

        This typically gets called by the Composer at the end.
        """
        if self.status is UpdateStatus.testing:
            for bug in self.bugs:
                log.debug('Adding testing comment to bugs for %s', self.alias)
                bug.testing(self)
        elif self.status is UpdateStatus.stable:
            if not self.close_bugs:
                for bug in self.bugs:
                    log.debug('Adding stable comment to bugs for %s', self.alias)
                    bug.add_comment(self)
            else:
                if self.type is UpdateType.security:
                    # Only close the tracking bugs
                    # https://github.com/fedora-infra/bodhi/issues/368#issuecomment-135155215
                    for bug in self.bugs:
                        if not bug.parent:
                            log.debug("Closing tracker bug %d" % bug.bug_id)
                            bug.close_bug(self)
                else:
                    for bug in self.bugs:
                        bug.close_bug(self)

    def status_comment(self, db):
        """
        Add a comment to this update about a change in status.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
        """
        if self.status is UpdateStatus.stable:
            self.comment(db, 'This update has been pushed to stable.',
                         author='bodhi')
        elif self.status is UpdateStatus.testing:
            self.comment(db, 'This update has been pushed to testing.',
                         author='bodhi')
        elif self.status is UpdateStatus.obsolete:
            self.comment(db, 'This update has been obsoleted.', author='bodhi')

    def send_update_notice(self):
        """Send e-mail notices about this update."""
        log.debug("Sending update notice for %s", self.alias)
        mailinglist = None
        sender = config.get('bodhi_email')
        if not sender:
            log.error(("bodhi_email not defined in configuration!  Unable "
                      "to send update notice"))
            return

        # eg: fedora_epel
        release_name = self.release.id_prefix.lower().replace('-', '_')
        if self.status is UpdateStatus.stable:
            mailinglist = config.get('%s_announce_list' % release_name)
        elif self.status is UpdateStatus.testing:
            mailinglist = config.get('%s_test_announce_list' % release_name)

        if mailinglist:
            for subject, body in mail.get_template(self, self.release.mail_template):
                mail.send_mail(sender, mailinglist, subject, body)
                notifications.publish(errata_schemas.ErrataPublishV1.from_dict(
                    dict(subject=subject, body=body, update=self)))
        else:
            log.error("Cannot find mailing list address for update notice")
            log.error("release_name = %r", release_name)

    def get_url(self):
        """
        Return the relative URL to this update.

        Returns:
            str: A URL.
        """
        return f'updates/{self.alias}'

    def abs_url(self, request=None):
        """
        Return the absolute URL to this update.

        Args:
            request (pyramid.request.Request or None): The current web request. Unused.
        """
        base = config['base_address']
        return urljoin(base, self.get_url())

    url = abs_url

    def __str__(self):
        """
        Return a string representation of this update.

        Returns:
            str: A string representation of the update.
        """
        nl = '\n'
        val = f"""{'=' * 80}
{nl.join(wrap(self.alias, width=79, initial_indent=' ' * 5, subsequent_indent=' ' * 5))}
{'=' * 80}
{'Release:':>12} {self.release.long_name}
{'Status:':>12} {self.status.description}
{'Type:':>12} {self.type.description}
{'Severity:':>12} {self.severity}
{'Karma:':>12} {self.karma}"""
        if self.critpath:
            val += f"{nl}{'Critpath:':>12} {self.critpath}"
        if self.request is not None:
            val += f"{nl}{'Request:':>12} {self.request.description}"
        if self.bugs:
            bugs = wrap_text(
                self.get_bugstring(show_titles=True), width=79,
                initial_indent=f"{'Bugs:':>12} ",
                subsequent_indent=f"{' ' * 13}")
            val += f"{nl}{bugs}"
        if self.notes:
            notes = wrap_text(
                markdown_to_text(self.notes).strip(), width=79,
                initial_indent=f"{'Notes:':>12} ",
                subsequent_indent=f"{' ' * 13}")
            val += f"{nl}{notes}"
        username = None
        if self.user:
            username = self.user.name
        val += f"""
{'Submitter:':>12} {username}
{'Submitted:':>12} {self.date_submitted}
"""
        if self.comments_since_karma_reset:
            comments_list = []
            for comment in reversed(self.comments_since_karma_reset):
                comments_list.append(f"{comment.user.name} - {comment.timestamp} "
                                     f"(karma {comment.karma})")
                if comment.text:
                    comments_list.append(comment.text)
            comments = wrap_text(
                '\n'.join(comments_list), width=79,
                initial_indent=f"{'Comments:':>12} ",
                subsequent_indent=f"{' ' * 13}")
            val += f"{comments}{nl}"
        val += f"{nl}  {self.abs_url()}"
        return val

    def update_bugs(self, bug_ids, session):
        """
        Make the update's bugs consistent with the given list of bug ids.

        Create any new bugs, and remove any missing ones. Destroy removed bugs that are no longer
        referenced anymore. If any associated bug is found to be a security bug, alter the update to
        be a security update.

        Args:
            bug_ids (list): A list of strings of bug ids to associate with this update.
            session (sqlalchemy.orm.session.Session): A database session.
        Returns:
            list: :class:`Bugs <Bug>` that are newly associated with the update.
        """
        to_remove = [bug for bug in self.bugs if bug.bug_id not in bug_ids]

        for bug in to_remove:
            self.bugs.remove(bug)
            if len(bug.updates) == 0:
                # Don't delete the Bug instance if there is any associated BugKarma
                if not session.query(BugKarma).filter_by(bug_id=bug.bug_id).count():
                    log.debug("Destroying stray Bugzilla #%d" % bug.bug_id)
                    session.delete(bug)
        session.flush()

        new = []
        for bug_id in bug_ids:
            bug = Bug.get(int(bug_id))
            if not bug:
                bug = Bug(bug_id=int(bug_id))
                session.add(bug)
                session.flush()
            if bug not in self.bugs:
                self.bugs.append(bug)
                new.append(bug.bug_id)
            if bug.security and self.type != UpdateType.security:
                self.type = UpdateType.security

        session.flush()
        return new

    def comment(self, session, text, karma=0, author=None, karma_critpath=0,
                bug_feedback=None, testcase_feedback=None, email_notification=True):
        """Add a comment to this update.

        If the karma reaches the 'stable_karma' value, then request that this update be marked
        as stable. If it reaches the 'unstable_karma' value, then unpush it (obsolete it).
        """
        if not author:
            raise ValueError('You must provide a comment author')

        # Listify these
        bug_feedback = bug_feedback or []
        testcase_feedback = testcase_feedback or []

        got_feedback = False
        for feedback_dict in (bug_feedback + testcase_feedback):
            if feedback_dict['karma'] != 0:
                got_feedback = True
                break

        if (not text and not karma and not karma_critpath and not got_feedback):
            raise ValueError('You must provide either some text or feedback')

        caveats = []

        if self.user.name == author:
            if karma != 0:
                karma = 0
                notice = 'You may not give karma to your own updates.'
                caveats.append({'name': 'karma', 'description': notice})

        try:
            user = session.query(User).filter_by(name=author).one()
        except NoResultFound:
            user = User(name=author)
            session.add(user)

        comment = Comment(text=text, karma=karma, karma_critpath=karma_critpath,
                          update=self, user=user)
        session.add(comment)

        if karma != 0:
            # Determine whether this user has already left karma, and if so what the most recent
            # karma value they left was. We should examine all but the most recent comment, since
            # that is the comment we just added.
            previous_karma = None
            for c in reversed(self.comments[:-1]):
                if c.user.name == author and c.karma:
                    previous_karma = c.karma
                    break
            if previous_karma and karma != previous_karma:
                caveats.append({
                    'name': 'karma',
                    'description': 'Your karma standing was reversed.',
                })
            else:
                log.debug('Ignoring duplicate %d karma from %s on %s', karma, author, self.alias)

            log.info("Updated %s karma to %d", self.alias, self.karma)

            if author not in config.get('system_users'):
                try:
                    self.check_karma_thresholds(session, 'bodhi')
                except LockedUpdateException:
                    pass
                except BodhiException as e:
                    # This gets thrown if the karma is pushed over the
                    # threshold, but it does not meet testing requirements
                    # for some reason (failed gating test...)
                    log.exception('Problem checking the karma threshold.')
                    caveats.append({
                        'name': 'karma', 'description': str(e),
                    })

        session.flush()

        for feedback_dict in bug_feedback:
            feedback = BugKarma(**feedback_dict)
            session.add(feedback)
            comment.bug_feedback.append(feedback)

        for feedback_dict in testcase_feedback:
            feedback = TestCaseKarma(**feedback_dict)
            session.add(feedback)
            comment.testcase_feedback.append(feedback)

        session.flush()

        # Publish to Fedora Messaging
        if author not in config.get('system_users'):
            notifications.publish(update_schemas.UpdateCommentV1.from_dict(
                {'comment': comment.__json__(), 'agent': author}))

        # Send a notification to everyone that has commented on this update
        people = set()
        for person in self.get_maintainers():
            if person.email:
                people.add(person.email)
            else:
                people.add(person.name)
        for comment in self.comments:
            if comment.user.name in ['anonymous', 'bodhi']:
                continue
            if comment.user.email:
                people.add(comment.user.email)
            else:
                people.add(comment.user.name)
        if email_notification:
            mail.send(people, 'comment', self, sender=None, agent=author)
        return comment, caveats

    def unpush(self, db):
        """
        Move this update back to its dist-fX-updates-candidate tag.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
        Raises:
            BodhiException: If the update isn't in testing.
        """
        log.debug("Unpushing %s", self.alias)
        koji = buildsys.get_session()

        if self.status is UpdateStatus.unpushed:
            log.debug("%s already unpushed", self.alias)
            return

        if self.status is not UpdateStatus.testing:
            raise BodhiException("Can't unpush a %s update"
                                 % self.status.description)

        self.untag(db, preserve_override=True)

        koji.multicall = True
        for build in self.builds:
            koji.tagBuild(self.release.candidate_tag, build.nvr, force=True)
        koji.multiCall()

        self.pushed = False
        self.status = UpdateStatus.unpushed
        self.request = None

    def revoke(self):
        """
        Remove pending request for this update.

        Raises:
            BodhiException: If the update doesn't have a request set, or if it is not in an expected
                status.
        """
        log.debug("Revoking %s", self.alias)

        if not self.request:
            raise BodhiException(
                "Can only revoke an update with an existing request")

        if self.status not in [UpdateStatus.pending, UpdateStatus.testing,
                               UpdateStatus.obsolete, UpdateStatus.unpushed]:
            raise BodhiException(
                "Can only revoke a pending, testing, unpushed, or obsolete "
                "update, not one that is %s" % self.status.description)

        # Remove the 'pending' koji tags from this update
        if self.request is UpdateRequest.testing:
            self.remove_tag(self.release.pending_signing_tag)
            self.remove_tag(self.release.pending_testing_tag)
        elif self.request is UpdateRequest.stable:
            self.remove_tag(self.release.pending_stable_tag)

        self.request = None

    def untag(self, db, preserve_override: bool = False):
        """
        Untag all of the :class:`Builds <Build>` in this update.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
            preserve_override: whether to preserve the override tag or not
        """
        log.info("Untagging %s", self.alias)
        koji = buildsys.get_session()
        tag_types, tag_rels = Release.get_tags()
        override_tags = self.release.inherited_override_tags + [self.release.override_tag]
        koji.multicall = True
        for build in self.builds:
            for tag in build.get_tags():
                # Only remove tags that we know about
                if tag in tag_rels:
                    if preserve_override and tag in override_tags:
                        log.info("Skipping override tag")
                    else:
                        koji.untagBuild(tag, build.nvr, force=True)
                else:
                    log.info("Skipping tag that we don't know about: %s" % tag)
        koji.multiCall()
        self.pushed = False

    def obsolete(self, db, newer=None):
        """
        Obsolete this update.

        Even though unpushing/obsoletion is an "instant" action, changes in the repository will not
        propagate until the next compose takes place.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
            newer (Update or None): If given, the update that has obsoleted this one. Defaults to
                ``None``.
        """
        log.debug("Obsoleting %s", self.alias)
        self.untag(db)
        self.status = UpdateStatus.obsolete
        self.request = None
        if newer:
            self.comment(db, "This update has been obsoleted by [%s](%s)." % (
                newer.nvr, newer.update.abs_url()), author='bodhi')
        else:
            self.comment(db, "This update has been obsoleted.", author='bodhi')

    def get_maintainers(self):
        """
        Return a list of maintainers who have commit access on the packages in this update.

        Returns:
            list: A list of :class:`Users <User>` who have commit access to all of the
                packages that are contained within this update.
        """
        return [self.user]

    @property
    def product_version(self):
        """
        Return a string of the product version that this update's release is associated with.

        The product version is a string, such as "fedora-26", and is used when querying Greenwave
        for test gating decisions.

        Returns:
            str: The product version associated with this Update's Release.
        """
        return self.release.long_name.lower().replace(' ', '-')

    def check_requirements(self, session, settings):
        """
        Check that an update meets all requirements to be pushed stable.

        See https://docs.fedoraproject.org/en-US/fesco/Updates_Policy .
        Deprecated in favor of meets_requirements_why property.

        Args:
            session (sqlalchemy.orm.session.Session): A database session. Unused.
            settings (bodhi.server.config.BodhiConfig): Bodhi's settings. Unused.
        Returns:
            tuple: A tuple containing (result, reason) where result is a bool
                and reason is a str.
        """
        warnings.warn(
            "check_requirements is deprecated, use meets_requirements_why instead",
            DeprecationWarning,
        )
        return self.meets_requirements_why

    def check_karma_thresholds(self, db, agent):
        """
        Check if we have reached some karma thresholds, and adjust state as necessary.

        If we receive negative karma, disable autopush (both time and karma). If we
        reach the karma autopush threshold (and the release is composed by Bodhi), set
        the request to stable. If we reach the auto-unpush threshold, obsolete the
        update. This method does **NOT** handle commenting and setting date_approved
        when the update reaches the manual push karma threshold. That is done by the
        approve_testing.py script.

        This method will call :meth:`set_request` if necessary. If the update is locked, it will
        ignore karma thresholds and raise an Exception.

        Args:
            db (sqlalchemy.orm.session.Session): A database session.
            agent (str): The username of the user who has provided karma.
        Raises:
            LockedUpdateException: If the update is locked.
        """
        # Raise Exception if the update is locked
        if self.locked:
            log.debug('%s locked. Ignoring karma thresholds.', self.alias)
            raise LockedUpdateException
        # Return if the status of the update is not in testing or pending
        if self.status not in (UpdateStatus.testing, UpdateStatus.pending):
            return
        # Also return if the status of the update is not in testing and the release is frozen
        if self.status != UpdateStatus.testing and self.release.state == ReleaseState.frozen:
            return
        # Obsolete if unstable karma threshold reached
        if self.unstable_karma and self.karma <= self.unstable_karma:
            log.info("Automatically obsoleting %s (reached unstable karma threshold)", self.alias)
            self.obsolete(db)
            notifications.publish(update_schemas.UpdateKarmaThresholdV1.from_dict(
                dict(update=self, status='unstable')))
        # If an update receives negative karma disable autopush
        # exclude rawhide updates see #4566
        if (self.autokarma or self.autotime) and self._composite_karma[1] != 0 and \
                self.request is not UpdateRequest.stable and \
                self.release.composed_by_bodhi:
            log.info("Disabling Auto Push since the update has received negative karma")
            self.autokarma = False
            self.autotime = False
            text = config.get('disable_automatic_push_to_stable')
            self.comment(db, text, author='bodhi')
        # If update with autopush reaches threshold, set request stable
        if self.stable_karma and self.karma >= self.stable_karma \
                and self.release.composed_by_bodhi and self.autokarma:
            # Updates for releases not "composed by Bodhi" (Rawhide,
            # ELN...) are pushed stable only by approve_testing.py
            if config.get('test_gating.required') and not self.test_gating_passed:
                log.info("%s reached stable karma threshold, but does not meet gating "
                         "requirements", self.alias)
                return
            if not self.date_approved:
                self.date_approved = datetime.now(timezone.utc)
            log.info("Automatically marking %s as stable", self.alias)
            self.set_request(db, UpdateRequest.stable, agent)
            notifications.publish(update_schemas.UpdateKarmaThresholdV1.from_dict(
                dict(update=self, status='stable')))

    @property
    def builds_json(self):
        """
        Return a JSON representation of this update's associated builds.

        Returns:
            str: A JSON list of the :class:`Builds <Build>` associated with this update.
        """
        return json.dumps([build.nvr for build in self.builds])

    @property
    def last_modified(self):
        """
        Return the last time this update was edited or created.

        This gets used for setting gating status - see _get_test_gating_status.

        Returns:
            datetime.datetime: The most recent time of modification or creation.
        Raises:
            ValueError: If the update has no timestamps set, which should not be possible.
        """
        # Prune out None values that have not been set
        possibilities = [self.date_submitted, self.date_modified]
        possibilities = [p for p in possibilities if p]

        if not possibilities:  # Should be un-possible.
            raise ValueError("Update has no timestamps set: %r" % self)

        possibilities.sort()  # Sort smallest to largest (oldest to newest)
        return possibilities[-1]  # Return the last one

    @property
    def critpath_approved(self):
        """
        Return whether or not this critpath update has been approved.

        Returns:
            bool: True if this update meets critpath testing requirements, False otherwise.
        """
        warnings.warn(
            "critpath_approved is deprecated, use meets_testing_requirements instead",
            DeprecationWarning,
        )
        return self.meets_testing_requirements

    @property
    def meets_requirements_why(self):
        """
        Return whether or not this update meets its release's testing requirements and why.

        Checks gating requirements and then minimum karma and wait requirements, see
        https://docs.fedoraproject.org/en-US/fesco/Updates_Policy . Note this is
        checking the minimum policy requirements for a manual push (as specified in
        the release configuration), not the per-update thresholds for an automatic push.
        Before updates-testing enablement the minimum wait will be 0, so unless the gating
        check fails, this will always return True.

        FIXME: we should probably wire up the test case and bug feedback requirements
        that are shown in the UI but not currently enforced.

        Returns:
            tuple: A tuple containing (result, reason) where result is a bool
                and reason is a str.
        """
        req_days = self.mandatory_days_in_testing
        req_karma = self.release.min_karma

        if config.get('test_gating.required'):
            tgs = self.test_gating_status
            if tgs in (TestGatingStatus.waiting, TestGatingStatus.queued, TestGatingStatus.running):
                return (False, "Required tests for this update are queued or running.")
            elif tgs == TestGatingStatus.greenwave_failed:
                return (False, "Greenwave failed to respond.")
            elif tgs == TestGatingStatus.passed:
                basemsg = "All required tests passed or were waived"
            elif tgs == TestGatingStatus.ignored:
                basemsg = "No checks required"
            else:
                return (False, "Required tests did not pass on this update.")
        else:
            basemsg = "Test gating is disabled,"

        if self.karma >= req_karma:
            return (True, basemsg + f" and the update has at least {req_karma} karma.")

        if not req_days:
            return (True, basemsg + " and there is no minimum wait set.")

        # Any update that reaches req_days has met the testing requirements.
        if self.days_in_testing >= req_days:
            return (True, basemsg + " and update meets the wait time requirement.")
        return (False,
                basemsg + f" but update has less than {req_karma} karma and has been in testing "
                f"less than {req_days} days.")

    @property
    def meets_testing_requirements(self):
        """
        Return whether or not this update meets its release's testing requirements.

        Same as meets_requirements_why, but without the reason.

        Returns:
            bool: True if the update meets testing requirements, False otherwise.
        """
        return self.meets_requirements_why[0]

    @property
    def has_stable_comment(self):
        """
        Return whether Bodhi has commented on the update that the requirements have been met.

        This is used to determine whether bodhi should add the comment
        about the Update's eligibility to be pushed, as we only want Bodhi
        to add the comment once.

        Returns:
            bool: See description above for what the bool might mean.
        """
        for comment in self.comments_since_karma_reset:
            if comment.user.name == 'bodhi' and \
               comment.text == config.get('testing_approval_msg'):
                return True
        return False

    @property
    def days_to_stable(self):
        """
        Return the number of days until an update can be pushed to stable.

        This method will return the number of days until an update can be pushed to stable, or 0.
        0 is returned if the update meets testing requirements already, if it doesn't have a
        "truthy" date_testing attribute, or if it's been in testing for the release's
        mandatory_days_in_testing or longer.

        Returns:
            int: The number of dates until this update can be pushed to stable, or 0 if it cannot be
                determined.
        """
        if not self.meets_testing_requirements and self.date_testing:
            num_days = (self.mandatory_days_in_testing - self.days_in_testing)
            if num_days > 0:
                return num_days
        return 0

    @property
    def days_in_testing(self):
        """
        Return the number of days that this update has been in testing.

        Returns:
            int: The number of days since this update's date_testing if it is set, else 0.
        """
        if self.date_testing:
            return (datetime.now(timezone.utc) - self.date_testing).days
        else:
            return 0

    @property
    def test_cases(self):
        """
        Return a list of all TestCase names associated with all packages in this update.

        Returns:
            list: A list of strings naming the :class:`TestCases <TestCase>` associated with
                this update.
        """
        tests = set()
        for build in self.builds:
            for test in build.testcases:
                tests.add(test.name)
        return sorted(list(tests))

    @property
    def full_test_cases(self):
        """
        Return a list of all TestCases associated with all packages in this update.

        Returns:
            list: A list of :class:`TestCases <TestCase>`.
        """
        tests = set()
        for build in self.builds:
            test_names = set()
            for test in build.testcases:
                if test.name not in test_names:
                    test_names.add(test.name)
                    tests.add(test)
        return sorted(list(tests), key=lambda testcase: testcase.name)

    @property
    def requested_tag(self):
        """
        Return the tag the update has requested.

        Returns:
            str: The Koji tag that corresponds to the update's current request.
        Raises:
            RuntimeError: If a Koji tag is unable to be determined.
        """
        tag = None
        if self.request is UpdateRequest.stable:
            tag = self.release.stable_tag
            # [No Frozen Rawhide] Move stable builds going to a pending
            # release to the Release.dist-tag
            if self.release.state is ReleaseState.pending:
                tag = self.release.dist_tag
        elif self.request == UpdateRequest.testing:
            tag = self.release.testing_tag
        elif self.request is UpdateRequest.obsolete:
            tag = self.release.candidate_tag
        if not tag:
            raise RuntimeError(
                f'Unable to determine requested tag for {self.alias}.')
        return tag

    def __json__(self, request=None):
        """
        Return a JSON representation of this update.

        Args:
            request (pyramid.request.Request or None): The current web request,
                or None. Passed on to :meth:`BodhiBase.__json__`.
        Returns:
            str: A JSON representation of this update.
        """
        result = super(Update, self).__json__(request=request)
        # Duplicate alias as updateid for backwards compat with bodhi1
        result['updateid'] = result['alias']
        # Include the karma total in the results
        result['karma'] = self.karma
        # Also, the Update content_type (derived from the builds content_types)
        result['content_type'] = self.content_type.value if self.content_type else None

        # For https://github.com/fedora-infra/bodhi/issues/270, throw the JSON
        # of the test cases in our output as well but take extra care to
        # short-circuit some of the insane recursion for
        # https://github.com/fedora-infra/bodhi/issues/343
        seen = [Package, TestCaseKarma]
        result['test_cases'] = [
            test._to_json(
                obj=test,
                seen=seen,
                request=request)
            for test in self.full_test_cases
        ]

        return result

    @staticmethod
    def comment_on_test_gating_status_change(target, value, old, initiator):
        """
        Place comment on the update when ``test_gating_status`` changes.

        Only notify the users by email if the new status is in ``failed``.

        Args:
            target (InstanceState): The state of the instance that has had a
                change to its test_gating_status attribute.
            value (EnumSymbol): The new value of the test_gating_status.
            old (EnumSymbol): The old value of the test_gating_status
            initiator (sqlalchemy.orm.attributes.Event): The event object that is initiating this
                transition.
        """
        instance = target.object

        if value != old:
            notify = value == TestGatingStatus.failed
            instance.comment(
                target.session,
                f"This update's test gating status has been changed to '{value}'.",
                author="bodhi",
                email_notification=notify,
            )

    def _build_group_test_message(self, agent="bodhi", retrigger=False):
        """
        Build the dictionary sent when an update is ready to be tested.

        This is used when we send notifications about an update being
        ready to be tested by any CI system - on update creation, any
        time the update is edited and its builds change, and if someone
        sends a Re-Trigger Tests request via the web UI or API.

        Args:
            agent (str): For the case where the message is sent as a test
                re-trigger request, the user who requested it. Otherwise,
                'bodhi'.
            retrigger (bool): Whether the message is sent as a test re-
                trigger request.
        Returns:
            dict: A dictionary corresponding to the message sent
        """
        builds = []
        for build in self.builds:
            builds.append({
                "type": "koji-build",
                "id": build.get_build_id(),
                "task_id": build.get_task_id(),
                "nvr": build.nvr,
            })

        artifact = {
            "type": "koji-build-group",
            "builds": builds,
        }
        return {
            "artifact": artifact,
            "update": self,
            'agent': agent,
            're-trigger': retrigger,
        }

    @staticmethod
    def _ready_for_testing(target, old):
        """
        Signal that the update is ready for testing.

        This happens when the update is created. The same message is
        also published when the update is edited and its builds change
        and when a "re-trigger tests" request is sent, but not by this
        method.

        Args:
            target (Update): The update that has been created.
            old (EnumSymbol): The old value of the Update.status.
        """
        if old == NEVER_SET:
            # This is the object initialization phase. This instance is not ready, don't create
            # the message now. This method will be called again at the end of __init__
            return
        if target.content_type != ContentType.rpm:
            return

        message = update_schemas.UpdateReadyForTestingV3.from_dict(
            message=target._build_group_test_message()
        )
        notifications.publish(message)


event.listen(
    Update.test_gating_status,
    'set',
    Update.comment_on_test_gating_status_change,
    active_history=True,
    raw=True,
)


class Compose(Base):
    """
    Express the status of an in-progress compose job.

    This object is used in a few ways:

        * It ensures that only one compose process runs per repo, serving as a compose "lock".
        * It marks which updates are part of a compose, serving as an update "lock".
        * It gives the compose process a place to log which step it is in, which will allow us to
          provide compose monitoring tools.

    Attributes:
        __exclude_columns__ (tuple): A tuple of columns to exclude when __json__() is called.
        __include_extras__ (tuple): A tuple of attributes to add when __json__() is called.
        __tablename__ (str): The name of the table in the database.
        checkpoints (str): A JSON serialized object describing the checkpoints the composer has
            reached.
        date_created (datetime.datetime): The time this Compose was created.
        error_message (str): An error message indicating what happened if the Compose failed.
        release_id (int): The primary key of the :class:`Release` that is being composed. Forms half
            of the primary key, with the other half being the ``request``.
        request (UpdateRequest): The request of the release that is being composed. Forms half of
            the primary key, with the other half being the ``release_id``.
        release (Release): The release that is being composed.
        state_date (datetime.datetime): The time of the most recent change to the state attribute.
        state (ComposeState): The state of the compose.
        updates (sqlalchemy.orm.collections.InstrumentedList): An iterable of updates included in
            this compose.
    """

    __exclude_columns__ = ('updates')
    # We need to include content_type and security so the composer can collate the Composes and so
    # it can pick the right composer class to use.
    __include_extras__ = ('content_type', 'security', 'update_summary')
    __tablename__ = 'composes'

    # These together form the primary key.
    release_id = Column(Integer, ForeignKey('releases.id'), primary_key=True, nullable=False)
    request = Column(UpdateRequest.db_type(), primary_key=True, nullable=False)

    # The parent class gives us an id primary key, but we'd rather have a "natural" primary key, so
    # let's override it and set to None.
    id = None
    # We could use the JSON type here, but that would require PostgreSQL >= 9.2.0. We don't really
    # need the ability to query inside this so the JSONB type probably isn't useful.
    checkpoints = Column(UnicodeText, nullable=False, default='{}')
    error_message = Column(UnicodeText)
    date_created = Column(TZDateTime, nullable=False,
                          default=partial(datetime.now, tz=timezone.utc))
    state_date = Column(TZDateTime, nullable=False, default=partial(datetime.now, tz=timezone.utc))

    release = relationship('Release', back_populates='composes')
    state = Column(ComposeState.db_type(), nullable=False, default=ComposeState.requested)

    updates = relationship(
        'Update',
        primaryjoin=("and_(foreign(Update.release_id)==Compose.release_id, "
                     "foreign(Update.request)==Compose.request, "
                     "Update.locked==True)"),
        passive_deletes=True, order_by='Update.date_submitted', overlaps='release',
        back_populates='compose')

    @property
    def content_type(self):
        """
        Return the content_type of this compose.

        Returns:
            (ContentType or None): The content type of this compose, or None if there are no
                associated :class:`Updates <Update>`.
        """
        if self.updates:
            return self.updates[0].content_type

    @classmethod
    def from_dict(cls, db, compose):
        """
        Return a :class:`Compose` instance from the given dict representation of it.

        Args:
            db (sqlalchemy.orm.session.Session): A database session to use to query for the compose.
            compose (dict): A dictionary representing the compose, in the format returned by
                :meth:`Compose.__json__`.
        Returns:
            bodhi.server.models.Compose: The requested compose instance.
        """
        return db.query(cls).filter_by(
            release_id=compose['release_id'],
            request=UpdateRequest.from_string(compose['request'])).one()

    @classmethod
    def from_updates(cls, updates):
        """
        Return a list of Compose objects to compose the given updates.

        The updates will be collated by release, request, and content type, and will be added to
        new Compose objects that match those groupings.

        Note that calling this will cause each of the updates to become locked once the transaction
        is committed.

        Args:
            updates (list): A list of :class:`Updates <Update>` that you wish to Compose.
        Returns:
            list: A list of new compose objects for the given updates.
        """
        work = {}
        for update in updates:
            if not update.request:
                log.info('%s request was revoked', update.alias)
                continue
            # ASSUMPTION: For now, updates can only be of a single type.
            ctype = None
            if not update.builds:
                log.info(f"No builds in {update.alias}. Skipping.")
                continue
            for build in update.builds:
                if ctype is None:
                    ctype = build.type
                elif ctype is not build.type:  # pragma: no cover
                    # This branch is not covered because the Update.validate_builds validator
                    # catches the same assumption breakage. This check here is extra for the
                    # time when someone adds multitype updates and forgets to update this.
                    raise ValueError(f'Builds of multiple types found in {update.alias}')
            # This key is just to insert things in the same place in the "work"
            # dict.
            key = '%s-%s' % (update.release.name, update.request.value)
            if key not in work:
                work[key] = cls(request=update.request, release_id=update.release.id,
                                release=update.release)
            # Lock the Update. This implicitly adds it to the Compose because the Update.compose
            # relationship joins on the Compose's compound pk for locked Updates.
            update.locked = True

        # We cast to a list here because a dictionary's values() method does not return a list in
        # Python 3 and the docblock states that a list is returned.
        return list(work.values())

    @property
    def security(self):
        """
        Return whether this compose is a security related compose or not.

        Returns:
            bool: ``True`` if any of the :class:`Updates <Update>` in this compose are marked as
                security updates.
        """
        for update in self.updates:
            if update.type is UpdateType.security:
                return True
        return False

    @staticmethod
    def update_state_date(target, value, old, initiator):
        """
        Update the ``state_date`` when the state changes.

        Args:
            target (Compose): The compose that has had a change to its state attribute.
            value (EnumSymbol): The new value of the state.
            old (EnumSymbol): The old value of the state
            initiator (sqlalchemy.orm.attributes.Event): The event object that is initiating this
                transition.
        """
        if value != old:
            target.state_date = datetime.now(timezone.utc)

    @property
    def update_summary(self):
        """
        Return a summary of the updates attribute, suitable for transmitting via the API.

        Returns:
            list: A list of dictionaries with keys 'alias' and 'title', indexing each update alias
                and title associated with this Compose.
        """
        return [{'alias': u.alias,
                'title': u.get_title(nvr=True, beautify=True)} for u in self.updates]

    def __json__(self, request=None, exclude=None, include=None, composer=False):
        """
        Serialize this compose in JSON format.

        Args:
            request (pyramid.request.Request or None): The current web request, or None.
            exclude (iterable or None): See superclass docblock.
            include (iterable or None): See superclass docblock.
            composer (bool): If True, increase the number of excluded attributes so that only the
                attributes required by the Composer to identify Composes are included. Defaults to
                False. If used, overrides exclude and include.
        Returns:
            str: A JSON representation of the Compose.
        """
        if composer:
            exclude = ('checkpoints', 'error_message', 'date_created', 'state_date', 'release',
                       'state', 'updates')
            # We need to include content_type and security so the composer can collate the Composes
            # and so it can pick the right composer class to use.
            include = ('content_type', 'security')
        return super(Compose, self).__json__(request=request, exclude=exclude, include=include)

    def __lt__(self, other):
        """
        Return ``True`` if this compose has a higher priority than the other.

        Args:
            other (Compose): Another compose we are comparing this compose to for sorting.
        Return:
            bool: ``True`` if this compose has a higher priority than the other, else ``False``.
        """
        if self.security and not other.security:
            return True
        if other.security and not self.security:
            return False
        if self.request == UpdateRequest.stable and other.request != UpdateRequest.stable:
            return True
        return False

    def __str__(self):
        """
        Return a human-readable representation of this compose.

        Returns:
            str: A string to be displayed to users describing this compose.
        """
        return '<Compose: {} {}>'.format(self.release.name, self.request.description)


event.listen(Compose.state, 'set', Compose.update_state_date, active_history=True)


# Used for many-to-many relationships between karma and a bug
class BugKarma(Base):
    """
    Karma for a bug associated with a comment.

    Attributes:
        karma (int): The karma associated with this bug and comment.
        comment (Comment): The comment this BugKarma is part of.
        bug (Bug): The bug this BugKarma pertains to.
    """

    __tablename__ = 'comment_bug_assoc'

    karma = Column(Integer, default=0)

    # Many-to-one relationships
    comment_id = Column(Integer, ForeignKey('comments.id'))
    comment = relationship('Comment', back_populates='bug_feedback')

    bug_id = Column(Integer, ForeignKey('bugs.bug_id'))
    bug = relationship('Bug', back_populates='feedback')


# Used for many-to-many relationships between karma and a TestCase
class TestCaseKarma(Base):
    """
    Karma for a TestCase associated with a comment.

    Attributes:
        karma (int): The karma associated with this TestCase comment.
        comment (Comment): The comment this TestCaseKarma is associated with.
        testcase (TestCase): The TestCase this TestCaseKarma pertains to.
    """

    __tablename__ = 'comment_testcase_assoc'

    karma = Column(Integer, default=0)

    # Many-to-one relationships
    comment_id = Column(Integer, ForeignKey('comments.id'))
    comment = relationship('Comment', back_populates='testcase_feedback')

    testcase_id = Column(Integer, ForeignKey('testcases.id'))
    testcase = relationship('TestCase', back_populates='feedback')


class Comment(Base):
    """
    An update comment.

    Attributes:
        karma (int): The karma associated with this comment. Defaults to 0.
        karma_critpath (int): The critpath karma associated with this comment. Defaults to 0.
            **DEPRECATED** no longer used in the UI
        text (str): The text of the comment.
        timestamp (datetime.datetime): The time the comment was created. Defaults to
            the return value of datetime.now(timezone.utc).
        update (Update): The update that this comment pertains to.
        user (User): The user who wrote this comment.
    """

    __tablename__ = 'comments'
    __exclude_columns__ = tuple()
    __get_by__ = ('id',)

    karma = Column(Integer, default=0)
    karma_critpath = Column(Integer, default=0)
    text = Column(UnicodeText, nullable=False)
    timestamp = Column(TZDateTime, default=partial(datetime.now, tz=timezone.utc))

    # One-to-many relationships
    bug_feedback = relationship('BugKarma', back_populates='comment',
                                cascade="all,delete,delete-orphan")

    testcase_feedback = relationship('TestCaseKarma', back_populates='comment',
                                     cascade="all,delete,delete-orphan")

    # Many-to-one relationships
    update_id = Column(Integer, ForeignKey('updates.id'), nullable=False, index=True)
    update = relationship('Update', back_populates='comments')

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='comments')

    def url(self) -> str:
        """
        Return a URL to this comment.

        Returns:
            A URL to this comment.
        """
        url = self.update.get_url() + '#comment-' + str(self.id)
        return url

    @property
    def unique_testcase_feedback(self) -> typing.List[TestCaseKarma]:
        """
        Return a list of unique :class:`TestCaseKarma` objects found in the testcase_feedback.

        This will filter out duplicates for :class:`TestCases <TestCase>`. It will return the
        correct number of TestCases in testcase_feedback as a list.

        Returns:
            A list of unique :class:`TestCaseKarma` objects associated with this comment.
        """
        feedbacks = self.testcase_feedback
        unique_feedbacks = set()
        filtered_feedbacks = list()
        for feedback in feedbacks:
            if feedback.testcase.name not in unique_feedbacks:
                unique_feedbacks.add(feedback.testcase.name)
                filtered_feedbacks.append(feedback)

        return filtered_feedbacks

    @property
    def rss_title(self) -> str:
        """
        Return a formatted title for the comment using update alias and comment id.

        Returns:
            A string representation of the comment for RSS feed.
        """
        return "{} comment #{}".format(self.update.alias, self.id)

    def __json__(self, *args, **kwargs) -> dict:
        """
        Return a JSON string representation of this comment.

        Args:
            args: A list of extra args to pass on to :meth:`BodhiBase.__json__`.
            kwargs: Extra kwargs to pass on to :meth:`BodhiBase.__json__`.
        Returns:
            A JSON-serializable dict representation of this comment.
        """
        result = super(Comment, self).__json__(*args, **kwargs)
        # Duplicate 'user' as 'author' just for backwards compat with bodhi1.
        # Things like the message schemas and fedbadges rely on this.
        if result['user']:
            result['author'] = result['user']['name']

        # Similarly, duplicate the update's alias as update_alias.
        result['update_alias'] = result['update']['alias']

        # Updates used to have a karma column which would be included in result['update']. The
        # column was replaced with a property, so we need to include it here for backwards
        # compatibility.
        result['update']['karma'] = self.update.karma

        return result

    def __str__(self) -> str:
        """
        Return a str representation of this comment.

        Returns:
            A str representation of this comment.
        """
        karma = '0'
        if self.karma != 0:
            karma = '%+d' % (self.karma,)
        return "%s - %s (karma: %s)\n%s" % (self.user.name, self.timestamp, karma, self.text)


class Bug(Base):
    """
    Represents a Bugzilla bug.

    Attributes:
        bug_id (int): The bug's id.
        title (str): The description of the bug.
        security (bool): True if the bug is marked as a security issue.
        parent (bool): True if this is a parent tracker bug for release-specific bugs.
    """

    __tablename__ = 'bugs'
    __exclude_columns__ = ('id', 'updates')
    __get_by__ = ('bug_id',)

    # Bug number. If None, assume ``url`` points to an external bug tracker
    bug_id = Column(Integer, unique=True)

    # The title of the bug
    title = Column(Unicode(255))

    # If we're dealing with a security bug
    security = Column(Boolean, default=False)

    # If this bug is a parent tracker bug for release-specific bugs
    parent = Column(Boolean, default=False)

    # Many-to-many relationships
    updates = relationship('Update', secondary=update_bug_table, back_populates='bugs')

    feedback = relationship('BugKarma', back_populates='bug')

    @property
    def url(self) -> str:
        """
        Return a URL to the bug.

        Returns:
            The URL to this bug.
        """
        return config['buglink'] % self.bug_id

    def update_details(self, bug: typing.Optional['bugzilla.bug.Bug'] = None) -> None:
        """
        Grab details from rhbz to populate our bug fields.

        This is typically called "offline" in the UpdatesHandler task.

        Args:
            bug: The Bug to retrieve details from Bugzilla about. If
                 None, self.bug_id will be used to retrieve the bug. Defaults to None.
        """
        bugs.bugtracker.update_details(bug, self)

    def default_message(self, update: Update) -> str:
        """
        Return a default comment to add to a bug with add_comment().

        Args:
            update: The update that is related to the bug.
        Returns:
            The default comment to add to the bug related to the given update.
        """
        install_msg = (
            f'Soon you\'ll be able to install the update with the following '
            f'command:\n`{update.install_command}`') if update.install_command else ''
        msg_data = {'update_title': update.get_title(delim=", ", nvr=True),
                    'update_beauty_title': update.get_title(beautify=True, nvr=True),
                    'update_alias': update.alias,
                    'repo': f'{update.release.long_name} {update.status.description}',
                    'install_instructions': install_msg,
                    'update_url': update.abs_url()}

        if update.status is UpdateStatus.stable:
            message = config['stable_bug_msg'].format(**msg_data)
        elif update.status is UpdateStatus.testing:
            if update.release.id_prefix == "FEDORA-EPEL":
                if 'testing_bug_epel_msg' in config:
                    template = config['testing_bug_epel_msg']
                else:
                    template = config['testing_bug_msg']
                    log.warning("No 'testing_bug_epel_msg' found in the config.")
            else:
                template = config['testing_bug_msg']
            message = template.format(**msg_data)
        else:
            raise ValueError(f'Trying to post a default comment to a bug, but '
                             f'{update.alias} is not in Stable or Testing status.')

        return message

    def add_comment(self, update: Update, comment: typing.Optional[str] = None) -> None:
        """
        Add a comment to the bug, pertaining to the given update.

        Args:
            update: The update that is related to the bug.
            comment: The comment to add to the bug. If None, a default message
                is added to the bug. Defaults to None.
        """
        if update.type is UpdateType.security and self.parent \
                and update.status is not UpdateStatus.stable:
            log.debug('Not commenting on parent security bug %s', self.bug_id)
        else:
            if not comment:
                comment = self.default_message(update)
            log.debug("Adding comment to Bug #%d: %s" % (self.bug_id, comment))
            bugs.bugtracker.comment(self.bug_id, comment)

    def testing(self, update: Update) -> None:
        """
        Change the status of this bug to ON_QA.

        Also, comment on the bug with some details on how to test and provide feedback for the given
        update.

        Args:
            update: The update associated with the bug.
        """
        # Skip modifying Security Response bugs for testing updates
        if update.type is UpdateType.security and self.parent:
            log.debug('Not modifying parent security bug %s', self.bug_id)
        else:
            comment = self.default_message(update)
            bugs.bugtracker.on_qa(self.bug_id, comment)

    def close_bug(self, update: Update) -> None:
        """
        Close the bug.

        Args:
            update: The update associated with the bug.
        """
        # Build a mapping of package names to build versions
        # so that .close() can figure out which build version fixes which bug.
        versions = dict([
            (b.nvr_name, b.nvr) for b in update.builds
        ])
        bugs.bugtracker.close(self.bug_id, versions=versions, comment=self.default_message(update))

    def modified(self, update: Update, comment: str) -> None:
        """
        Change the status of this bug to MODIFIED unless it is a parent security bug.

        Also, comment on the bug stating that an update has been submitted.

        Args:
            update: The update that is associated with this bug.
            comment: A comment to leave on the bug when modifying it.
        """
        if update.type is UpdateType.security and self.parent:
            log.debug('Not modifying parent security bug %s', self.bug_id)
        else:
            bugs.bugtracker.modified(self.bug_id, comment)


user_group_table = Table('user_group_table', Base.metadata,
                         Column('user_id', Integer, ForeignKey('users.id')),
                         Column('group_id', Integer, ForeignKey('groups.id')))


class User(Base):
    """
    A Bodhi user.

    Attributes:
        name (str): The username.
        email (str): An e-mail address for the user.
        comments (sqlalchemy.orm.dynamic.AppenderQuery): An iterable of :class:`Comments <Comment>`
            the user has written.
        updates (sqlalchemy.orm.dynamic.AppenderQuery): An iterable of :class:`Updates <Update>` the
            user has created.
        groups (sqlalchemy.orm.collections.InstrumentedList): An iterable of :class:`Groups <Group>`
            the user is a member of.
    """

    __tablename__ = 'users'
    __exclude_columns__ = ('comments', 'updates', 'buildroot_overrides')
    __include_extras__ = ('avatar', 'openid')
    __get_by__ = ('name',)

    name = Column(Unicode(64), unique=True, nullable=False)
    email = Column(UnicodeText)

    # One-to-many relationships
    comments = relationship('Comment', back_populates='user', lazy='dynamic')

    updates = relationship('Update', back_populates='user', lazy='dynamic')

    buildroot_overrides = relationship('BuildrootOverride', back_populates='submitter')

    # Many-to-many relationships
    groups = relationship('Group', secondary=user_group_table, back_populates='users')

    def avatar(self, request: 'pyramid.request') -> typing.Union[str, None]:
        """
        Return a URL for the User's avatar, or None if request is falsey.

        Args:
            request: The current web request.
        Returns:
            A URL for the User's avatar, or None if request is falsey.
        """
        if not request:
            return None
        context = dict(request=request)
        return get_avatar(context=context, username=self.name, usermail=self.email, size=24)

    def openid(self, request: 'pyramid.request') -> str:
        """
        Return an openid identity URL.

        Args:
            request: The current web request.
        Returns:
            The openid identity URL for the User object.
        """
        if not request:
            return None
        template = request.registry.settings.get('openid_template')
        return template.format(username=self.name)


class Group(Base):
    """
    A group of users.

    Attributes:
        name (str): The name of the Group.
        users (sqlalchemy.orm.collections.InstrumentedList): An iterable of the
            :class:`Users <User>` who are in the group.
    """

    __tablename__ = 'groups'
    __get_by__ = ('name',)
    __exclude_columns__ = ('id',)

    name = Column(Unicode(64), unique=True, nullable=False)

    # Many-to-many relationships
    users = relationship("User", secondary=user_group_table, back_populates='groups')


class BuildrootOverride(Base):
    """
    This model represents a Koji buildroot override.

    A buildroot override is a way to add a build to the Koji buildroot (the set of packages used
    to build a package) manually. Normally, builds are only available after they are pushed to
    "stable", but this allows a build to be added to the buildroot immediately. This is useful
    for updates that depend on each other to be built.

    Attributes:
        notes (str): A text field that holds arbitrary notes about the buildroot override.
        submission_date (DateTime): The date that the buildroot override was submitted.
        expiration_date (DateTime): The date that the buildroot override expires.
        expired_date (DateTime): The date that the buildroot override expired.
        build_id (int): The primary key of the :class:`Build` this override is related to.
        build (Build): The build this override is related to.
        submitter_id (int): The primary key of the :class:`User` this override was created by.
        submitter (User): The user this override was created by.
    """

    __tablename__ = 'buildroot_overrides'
    __include_extras__ = ('nvr',)
    __get_by__ = ('build_id',)

    notes = Column(UnicodeText, nullable=False)

    submission_date = Column(TZDateTime, default=partial(datetime.now, tz=timezone.utc),
                             nullable=False)
    expiration_date = Column(TZDateTime, nullable=False)
    expired_date = Column(TZDateTime)

    # Many-to-one relationships
    build_id = Column(Integer, ForeignKey('builds.id'), nullable=False)
    build = relationship('Build', lazy='joined', innerjoin=True,
                         back_populates='override')

    submitter_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    submitter = relationship('User', lazy='joined', innerjoin=True,
                             back_populates='buildroot_overrides')

    @property
    def nvr(self) -> str:
        """
        Return the NVR of the :class:`Build` associated with this override.

        Returns:
            The override's :class:`Build's <Build>` NVR.
        """
        return self.build.nvr

    @classmethod
    def new(cls, request: 'pyramid.request', **data) -> 'BuildrootOverride':
        """
        Create a new buildroot override.

        Args:
            request: The current web request.
            data: A dictionary of all the attributes to be used on the new override.
        Returns:
            The newly created BuildrootOverride instance.
        """
        db = request.db

        build = data['build']

        if build.override is not None:
            request.errors.add('body', 'nvr',
                               '%s is already in a override' % build.nvr)
            return

        old_build = db.query(Build).filter(
            and_(
                Build.package_id == build.package_id,
                Build.release_id == build.release_id)).first()

        if old_build is not None and old_build.override is not None:
            # There already is a buildroot override for an older build of this
            # package in this release. Expire it
            log.debug(f"Expiring BRO for {old_build.nvr} because it's superseded by {build.nvr}.")
            old_build.override.expire()
            db.add(old_build.override)

        override = cls(**data)
        override.enable()
        db.add(override)
        db.flush()

        return override

    @classmethod
    def edit(cls, request: 'pyramid.request', **data) -> 'BuildrootOverride':
        """
        Edit an existing buildroot override.

        Args:
            request: The current web request.
            data: The changed being made to the BuildrootOverride.
        Returns:
            The new updated override.
        """
        db = request.db
        edited = data.pop('edited')
        override = cls.get(edited.id)

        if override is None:
            request.errors.add('body', 'edited',
                               'No buildroot override for this build')
            return

        override.submitter = data['submitter']
        override.notes = data['notes']
        override.expiration_date = data['expiration_date']
        if 'submission_date' in data:
            override.submission_date = data['submission_date']

        now = datetime.now(timezone.utc)

        if override.expired_date is not None and override.expiration_date > now:
            # Buildroot override had expired, we need to unexpire it
            override.enable()

        elif data['expired']:
            log.debug(f"Expiring BRO for {override.build.nvr} because it was edited.")
            override.expire()

        db.add(override)
        db.flush()

        return override

    def enable(self) -> None:
        """Mark the BuildrootOverride as enabled."""
        koji_session = buildsys.get_session()
        for tag in self.build.release.inherited_override_tags + [self.build.release.override_tag]:
            koji_session.tagBuild(tag, self.build.nvr)

        notifications.publish(override_schemas.BuildrootOverrideTagV1.from_dict(
            dict(override=self)))

        self.expired_date = None

    def expire(self) -> None:
        """Mark the BuildrootOverride as expired."""
        if self.expired_date is not None:
            return

        koji_session = buildsys.get_session()
        for tag in self.build.release.inherited_override_tags + [self.build.release.override_tag]:
            try:
                koji_session.untagBuild(tag, self.build.nvr, strict=True)
            except Exception as e:
                log.error(f"Unable to untag override {self.build.nvr} from {tag}: '{e}'")
        self.expired_date = datetime.now(timezone.utc)

        notifications.publish(override_schemas.BuildrootOverrideUntagV1.from_dict(
            {'override': self}))
