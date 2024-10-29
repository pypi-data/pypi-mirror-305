# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import enum
import logging
import posixpath

from datetime import datetime, timezone
from typing import Optional

import attr
import attr.validators
import cattr

from pyparsing import Literal as L, Word, Optional as OptionalItem
from pyparsing import printables as _printables, rest_of_line
from pyparsing import ParseException

from linehaul.ua import UserAgent, parser as user_agents


logger = logging.getLogger(__name__)


_cattr = cattr.Converter()
_cattr.register_structure_hook(
    datetime,
    lambda d, t: datetime.strptime(d[5:-4], "%d %b %Y %H:%M:%S").replace(
        tzinfo=timezone.utc
    ),
)


class UnparseableEvent(Exception):
    pass


class _NullValue:
    pass


NullValue = _NullValue()


printables = "".join(set(_printables + " " + "\t") - {"|", "@"})

PIPE = L("|").suppress()

AT = L("@").suppress()

NULL = L("(null)")
NULL.set_parse_action(lambda s, l, t: NullValue)

TIMESTAMP = Word(printables).set_name("Timestamp")
TIMESTAMP = TIMESTAMP.set_results_name("timestamp")

COUNTRY_CODE = Word(printables).set_name("Country Code")
COUNTRY_CODE = COUNTRY_CODE.set_results_name("country_code")

URL = Word(printables).set_name("URL")
URL = URL.set_results_name("url")

REQUEST = TIMESTAMP + PIPE + OptionalItem(COUNTRY_CODE) + PIPE + URL

PROJECT_NAME = NULL | Word(printables)
PROJECT_NAME = PROJECT_NAME.set_results_name("project_name")
PROJECT_NAME.set_name("Project Name")

VERSION = NULL | Word(printables)
VERSION = VERSION.set_results_name("version")
VERSION.set_name("Version")

PACKAGE_TYPE = NULL | (
    L("sdist")
    | L("bdist_wheel")
    | L("bdist_dmg")
    | L("bdist_dumb")
    | L("bdist_egg")
    | L("bdist_msi")
    | L("bdist_rpm")
    | L("bdist_wininst")
)
PACKAGE_TYPE = PACKAGE_TYPE.set_results_name("package_type")
PACKAGE_TYPE.set_name("Package Type")

PROJECT = PROJECT_NAME + PIPE + VERSION + PIPE + PACKAGE_TYPE

TLS_PROTOCOL = NULL | Word(printables)
TLS_PROTOCOL = TLS_PROTOCOL.set_results_name("tls_protocol")
TLS_PROTOCOL.set_name("TLS Protocol")

TLS_CIPHER = NULL | Word(printables)
TLS_CIPHER = TLS_CIPHER.set_results_name("tls_cipher")
TLS_CIPHER.set_name("TLS Cipher")

TLS = TLS_PROTOCOL + PIPE + TLS_CIPHER

USER_AGENT = rest_of_line
USER_AGENT = USER_AGENT.set_results_name("user_agent")
USER_AGENT.set_name("UserAgent")

V1_HEADER = OptionalItem(L("1").suppress() + AT)

MESSAGE_v1 = V1_HEADER + REQUEST + PIPE + PROJECT + PIPE + USER_AGENT
MESSAGE_v1.leave_whitespace()

V2_HEADER = L("2").suppress() + AT

MESSAGE_v2 = V2_HEADER + REQUEST + PIPE + TLS + PIPE + PROJECT + PIPE + USER_AGENT
MESSAGE_v2.leave_whitespace()

V3_HEADER = L("download")
MESSAGE_v3 = (
    V3_HEADER + PIPE + REQUEST + PIPE + TLS + PIPE + PROJECT + PIPE + USER_AGENT
)

SIMPLE_HEADER = L("simple")
MESSAGE_SIMPLE = (
    SIMPLE_HEADER + PIPE + REQUEST + PIPE + TLS + PIPE + PIPE + PIPE + PIPE + USER_AGENT
)

MESSAGE = MESSAGE_SIMPLE | MESSAGE_v3 | MESSAGE_v2 | MESSAGE_v1


@enum.unique
class PackageType(enum.Enum):
    bdist_dmg = "bdist_dmg"
    bdist_dumb = "bdist_dumb"
    bdist_egg = "bdist_egg"
    bdist_msi = "bdist_msi"
    bdist_rpm = "bdist_rpm"
    bdist_wheel = "bdist_wheel"
    bdist_wininst = "bdist_wininst"
    sdist = "sdist"


@attr.s(slots=True, frozen=True)
class File:
    filename = attr.ib(validator=attr.validators.instance_of(str))
    project = attr.ib(validator=attr.validators.instance_of(str))
    version = attr.ib(validator=attr.validators.instance_of(str))
    type = attr.ib(type=PackageType)


@attr.s(slots=True, frozen=True)
class Download:
    timestamp = attr.ib(type=datetime)
    url = attr.ib(validator=attr.validators.instance_of(str))
    project = attr.ib(validator=attr.validators.instance_of(str))
    file = attr.ib(type=File)
    tls_protocol = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    tls_cipher = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    country_code = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    details = attr.ib(type=Optional[UserAgent], default=None)


@attr.s(slots=True, frozen=True)
class Simple:
    timestamp = attr.ib(type=datetime)
    url = attr.ib(validator=attr.validators.instance_of(str))
    project = attr.ib(validator=attr.validators.instance_of(str))
    tls_protocol = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    tls_cipher = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    country_code = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    details = attr.ib(type=Optional[UserAgent], default=None)


def _value_or_none(value):
    if value is NullValue or value == "":
        return None
    else:
        return value


def parse(message):
    try:
        parsed = MESSAGE.parse_string(message, parseAll=True)
    except ParseException as exc:
        raise UnparseableEvent("{!r} {}".format(message, exc)) from None

    data = {}
    data["timestamp"] = parsed.timestamp
    data["tls_protocol"] = _value_or_none(parsed.tls_protocol)
    data["tls_cipher"] = _value_or_none(parsed.tls_cipher)
    data["country_code"] = _value_or_none(parsed.country_code)
    data["url"] = parsed.url
    data["file"] = {}
    data["file"]["filename"] = posixpath.basename(parsed.url)
    data["file"]["project"] = _value_or_none(parsed.project_name)
    data["file"]["version"] = _value_or_none(parsed.version)
    data["file"]["type"] = _value_or_none(parsed.package_type)

    if parsed[0] == "download":
        data["project"] = _value_or_none(parsed.project_name)
        result = _cattr.structure(data, Download)
    elif parsed[0] == "simple":
        data["project"] = parsed.url.split("/")[2]
        result = _cattr.structure(data, Simple)
    else:
        result = _cattr.structure(data, Download)

    try:
        ua = user_agents.parse(parsed.user_agent)
        if ua is None:
            return  # Ignored user agents mean we'll skip trying to log this event
    except user_agents.UnknownUserAgentError:
        pass
    else:
        result = attr.evolve(result, details=ua)

    return result
