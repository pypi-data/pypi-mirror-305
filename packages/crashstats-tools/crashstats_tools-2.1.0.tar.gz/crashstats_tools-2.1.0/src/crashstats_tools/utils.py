# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import csv
import datetime
from functools import total_ordering
import inspect
import io
import json
import os
import re
import string
from typing import Any, Dict, Generator, Iterable, List
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter, Retry
from rich.console import Console

from crashstats_tools import __version__


DEFAULT_HOST = "https://crash-stats.mozilla.org"


WHITESPACE_TO_ESCAPE = [("\t", "\\t"), ("\r", "\\r"), ("\n", "\\n")]


def dbg(*args):
    """Utility for printing debug output when debugging.

    Prints the filename and line number and then a stringified list of the
    args.

    """
    console = Console(stderr=True, tab_size=None)
    callframe = inspect.currentframe().f_back
    fn = callframe.f_code.co_filename.split(os.sep)[-1]
    lineno = callframe.f_lineno
    str_args = ", ".join(f"{arg!r}" for arg in args)
    console.print(f"dbg: [yellow]{fn}:{lineno}[/yellow] {str_args}")


class ConsoleLogger:
    """Logs to a click console."""

    def __init__(self, console):
        self.console = console

    def log(self, level, msg, *args, **kwargs):
        # NOTE(willkg): kwargs are currently ignored
        self.console.print(msg % args)

    def debug(self, msg, *args, **kwargs):
        self.log(10, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log(20, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log(30, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log(40, msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        # NOTE(willkg): exception doesn't add exception information--currently,
        # it's just an alias for error
        self.log(40, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.log(50, msg, *args, **kwargs)


def escape_whitespace(text):
    """Escapes whitespace characters."""
    text = text or ""
    for s, replace in WHITESPACE_TO_ESCAPE:
        text = text.replace(s, replace)
    return text


def escape_pipes(text):
    """Escape pipe characters."""
    text = text or ""
    return text.replace("|", "\\|")


def sanitize_text(item):
    """Sanitizes text dropping all non-printable characters."""
    if not isinstance(item, str):
        return item
    text = "".join([c for c in item if c in string.printable])
    return text


class JsonDTEncoder(json.JSONEncoder):
    """JSON encoder that handles datetimes

    >>> json.dumps(some_data, cls=JsonDTEncoder)
    ...

    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S.%f")
        return json.JSONEncoder.default(self, obj)


class HTTPAdapterWithTimeout(HTTPAdapter):
    """HTTPAdapter with a default timeout

    This allows you to set a default timeout when creating the adapter.
    It can be overridden here as well as when doing individual
    requests.

    :arg varies default_timeout: number of seconds before timing out

        This can be a float or a (connect timeout, read timeout) tuple
        of floats.

        Defaults to 5.0 seconds.

    """

    def __init__(self, *args, **kwargs):
        self._default_timeout = kwargs.pop("default_timeout", 5.0)
        super().__init__(*args, **kwargs)

    def send(self, *args, **kwargs):
        # If there's a timeout, use that. Otherwise, use the default.
        kwargs["timeout"] = kwargs.get("timeout") or self._default_timeout
        return super().send(*args, **kwargs)


def session_with_retries(
    total_retries=10,
    backoff_factor=0.2,
    status_forcelist=(429, 500, 502, 504),
    default_timeout=5.0,
):
    """Returns session that retries on HTTP error codes with default timeout

    :arg int total_retries: total number of times to retry

    :arg float backoff_factor: number of seconds to increment by between
        attempts

        For example, 0.1 will back off 0.1s, then 0.2s, then 0.3s, ...

    :arg tuple of HTTP codes status_forcelist: tuple of HTTP codes to
        retry on

    :arg varies default_timeout: number of seconds before timing out

        This can be a float or a (connect timeout, read timeout) tuple
        of floats.

    :returns: a requests Session instance

    """
    retries = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=list(status_forcelist),
    )

    session = requests.Session()

    # Set the User-Agent header so we can distinguish our stuff from other stuff
    session.headers.update({"User-Agent": f"crashstats-tools/{__version__}"})

    adapter = HTTPAdapterWithTimeout(
        max_retries=retries, default_timeout=default_timeout
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


class BadRequest(Exception):
    """HTTP Request is not valid."""


class BadAPIToken(Exception):
    """API Token is not valid."""


def http_get(url, params, api_token=None):
    """Retrieve data at url with params and api_token.

    :raises CrashDoesNotExist:
    :raises BadAPIToken:

    :returns: requests Response

    """
    if api_token:
        headers = {"Auth-Token": api_token}
    else:
        headers = {}

    session = session_with_retries()

    resp = session.get(url, params=params, headers=headers)

    # Handle 403 so we can provide the user more context
    if api_token and resp.status_code == 403:
        try:
            error = resp.json().get("error", "No error provided")
        except requests.exceptions.JSONDecodeError:
            error = resp.text or "no response provided"

        raise BadAPIToken(f"HTTP {resp.status_code}: {error}")

    # Handle 400 which indicates a problem with the request
    if resp.status_code == 400:
        try:
            error = resp.json().get("error", "No error provided")
        except requests.exceptions.JSONDecodeError:
            error = resp.text or "no response provided"

        raise BadRequest(f"HTTP {resp.status_code}: {error}")

    # Raise an error for any other non-200 response
    resp.raise_for_status()
    return resp


def http_post(url, data, api_token=None):
    """POST data at url with api_token.

    :raises BadAPIToken:

    :returns: requests Response

    """
    if api_token:
        headers = {"Auth-Token": api_token}
    else:
        headers = {}

    session = session_with_retries()

    resp = session.post(url, data=data, headers=headers)

    # Handle 403 so we can provide the user more context
    if api_token and resp.status_code == 403:
        raise BadAPIToken(resp.json().get("error", "No error provided"))

    # Raise an error for any other non-200 response
    resp.raise_for_status()
    return resp


@total_ordering
class Infinity:
    """Infinity is greater than anything else except other Infinities

    NOTE(willkg): There are multiple infinities and not all infinities are
    equal, so what we're doing here is wrong, but it's helpful. We can rename
    it if someone gets really annoyed.

    """

    def __eq__(self, obj):
        return isinstance(obj, Infinity)

    def __lt__(self, obj):
        return False

    def __repr__(self):
        return "Infinity"

    def __sub__(self, obj):
        if isinstance(obj, Infinity):
            return 0
        return self

    def __rsub__(self, obj):
        # We don't need to deal with negative infinities, so let's not
        raise ValueError("This Infinity does not support right-hand-side")


# For our purposes, there is only one infinity
INFINITY = Infinity()


@total_ordering
class AlwaysFirst:
    """This item is always first."""

    def __eq__(self, other):
        # Two AlwaysFirst instances are always equal
        return type(other) is type(self)

    def __lt__(self, other):
        # This is always less than other
        return True


@total_ordering
class AlwaysLast:
    """This item is always last."""

    def __eq__(self, other):
        # Two AlwaysLast instances are always equal
        return type(other) is type(self)

    def __lt__(self, other):
        # This is always greater than other
        return False


class InvalidArg(Exception):
    """Denotes an invalid command line argument."""


def parse_args(args):
    """Convert command line arguments to supersearch arguments."""
    params = {}

    while args:
        field = args.pop(0)
        if not field.startswith("--"):
            raise InvalidArg("unknown argument %r" % field)
            return 1

        if "=" in field:
            field, value = field.split("=", 1)
        else:
            if args:
                value = args.pop(0)
            else:
                raise InvalidArg("arg %s has no value" % field)

        # Remove the -- from the beginning of field
        field = field[2:]

        # Remove quotes from value if they exist
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        params.setdefault(field, []).append(value)
    return params


CRASH_ID_RE = re.compile(
    r"""
    ^
    [a-f0-9]{8}-
    [a-f0-9]{4}-
    [a-f0-9]{4}-
    [a-f0-9]{4}-
    [a-f0-9]{6}
    [0-9]{6}      # date in YYMMDD
    $
""",
    re.VERBOSE,
)


def is_crash_id_valid(crash_id):
    """Returns whether this is a valid crash id

    :arg str crash_id: the crash id in question

    :returns: True if it's valid, False if not

    """
    return bool(CRASH_ID_RE.match(crash_id))


def parse_crash_id(item):
    """Returns a crash id from a number of formats.

    This handles the following three forms of crashids:

    * CRASHID
    * bp-CRASHID
    * http[s]://HOST[:PORT]/report/index/CRASHID

    :arg str item: the thing to parse a crash id from

    :returns: crash id as str or None

    :raises ValueError: if the crash id isn't recognized

    """
    if is_crash_id_valid(item):
        return item

    if item.startswith("bp-") and is_crash_id_valid(item[3:]):
        return item[3:]

    if item.startswith("http"):
        parsed = urlparse(item)
        path = parsed.path
        if path.startswith("/report/index"):
            crash_id = path.split("/")[-1]
            if is_crash_id_valid(crash_id):
                return crash_id

    raise ValueError(f"Not a valid crash id: {item}")


class MissingField(Exception):
    """Denotes a missing field."""


def tableize_csv(
    headers: List[str], data: Iterable[Dict[str, Any]], show_headers: bool = True
) -> Generator[str, None, None]:
    """Generate output for a table in csv.

    :param headers: headers of the table
    :param data: rows of the table

    :returns: generator of strings

    """
    buffer = io.StringIO()
    csvwriter = csv.writer(buffer)
    for item_i, item in enumerate(data):
        if item_i == 0:
            for field in headers:
                if field not in item:
                    raise MissingField(field)
            if show_headers:
                csvwriter.writerow([escape_whitespace(str(item)) for item in headers])

        row = [escape_whitespace(str(item.get(field, ""))) for field in headers]
        if row:
            csvwriter.writerow(row)

    for line in buffer.getvalue().splitlines():
        yield line


def tableize_tab(
    headers: List[str], data: Iterable[Dict[str, Any]], show_headers: bool = True
) -> Generator[str, None, None]:
    """Generate output for a table using tab delimiters.

    :param headers: headers of the table
    :param data: rows of the table

    :returns: generator of strings

    """
    for item_i, item in enumerate(data):
        if item_i == 0:
            for field in headers:
                if field not in item:
                    raise MissingField(field)
            if show_headers:
                yield "\t".join([escape_whitespace(str(item)) for item in headers])

        row = [escape_whitespace(str(item.get(field, ""))) for field in headers]
        yield "\t".join(row) or "<no data>"


def tableize_markdown(
    headers: List[str], data: Iterable[Dict[str, Any]], show_headers: bool = True
) -> Generator[str, None, None]:
    """Generate output for a table using markdown.

    :param headers: headers of the table
    :param data: rows of the table

    :returns: generator of strings

    """
    for item_i, item in enumerate(data):
        if item_i == 0:
            for field in headers:
                if field not in item:
                    raise MissingField(field)

            if show_headers:
                yield " | ".join([str(header) for header in headers])
                yield " | ".join(["-" * len(str(item)) for item in headers])

        row = [escape_pipes(escape_whitespace(str(item[field]))) for field in headers]
        yield " | ".join(row) or "<no data>"


RELATIVE_RE = re.compile(r"(\d+)([hdw])", re.IGNORECASE)


def parse_relative_date(text):
    """Takes a relative date specification and returns a timedelta."""
    if not text or not isinstance(text, str):
        raise ValueError(f"'{text}' is not a valid relative date.")

    parsed = RELATIVE_RE.match(text)
    if parsed is None:
        raise ValueError(f"'{text}' is not a valid relative date.")

    count = int(parsed.group(1))
    unit = parsed.group(2)

    unit_to_arg = {"h": "hours", "d": "days", "w": "weeks"}
    return datetime.timedelta(**{unit_to_arg[unit]: count})


def thing_to_key(item):
    """Returns a sorting key for the item

    This causes "--" to always be first and "total" to always
    be last.

    For lists/tuples, this picks the first item.

    :returns: a key

    """
    if isinstance(item, (list, tuple)):
        item = item[0]
    if item == "--":
        return AlwaysFirst()
    if item == "total":
        return AlwaysLast()
    return item
