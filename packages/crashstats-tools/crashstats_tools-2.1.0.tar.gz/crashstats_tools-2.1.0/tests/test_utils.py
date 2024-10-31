# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime
import inspect
import operator

import pytest

from crashstats_tools.utils import (
    escape_pipes,
    escape_whitespace,
    INFINITY,
    is_crash_id_valid,
    parse_args,
    parse_crash_id,
    parse_relative_date,
    tableize_markdown,
    tableize_tab,
)


@pytest.mark.parametrize(
    "text, expected",
    [
        (None, ""),
        ("", ""),
        ("abc", "abc"),
        ("abc\tdef", "abc\\tdef"),
        ("abc\rdef", "abc\\rdef"),
        ("abc\ndef", "abc\\ndef"),
    ],
)
def test_escape_whitespace(text, expected):
    assert escape_whitespace(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (None, ""),
        ("", ""),
        ("abc", "abc"),
        ("abc|def", "abc\\|def"),
    ],
)
def test_escape_pipes(text, expected):
    assert escape_pipes(text) == expected


@pytest.mark.parametrize(
    "crashid, expected",
    [
        ("", False),
        ("aaa", False),
        ("de1bb258cbbf4589a67334f800160918", False),
        ("DE1BB258-CBBF-4589-A673-34F800160918", False),
        ("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", False),
        ("00000000-0000-0000-0000-000000000000", True),
    ],
)
def test_validate_crash_id(crashid, expected):
    assert is_crash_id_valid(crashid) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ([], {}),
        (["--foo", "bar"], {"foo": ["bar"]}),
        (["--foo=bar"], {"foo": ["bar"]}),
        (["--foo=bar1", "--foo=bar2"], {"foo": ["bar1", "bar2"]}),
    ],
)
def test_parse_args(args, expected):
    assert parse_args(args) == expected


@pytest.mark.parametrize(
    "item, expected",
    [
        (
            "0b794045-87ec-4649-9ce1-73ec10191120",
            "0b794045-87ec-4649-9ce1-73ec10191120",
        ),
        (
            "bp-0b794045-87ec-4649-9ce1-73ec10191120",
            "0b794045-87ec-4649-9ce1-73ec10191120",
        ),
        (
            "https://crash-stats.mozilla.org/report/index/0b794045-87ec-4649-9ce1-73ec10191120",
            "0b794045-87ec-4649-9ce1-73ec10191120",
        ),
    ],
)
def test_parse_crash_id(item, expected):
    assert parse_crash_id(item) == expected


@pytest.mark.parametrize("item", ["", "foo"])
def test_parse_crash_id_badids(item):
    with pytest.raises(ValueError):
        parse_crash_id(item)


@pytest.mark.parametrize(
    "oper, rhs, expected",
    [
        # Infinity == x
        (operator.eq, 10000, False),
        (operator.eq, INFINITY, True),
        # Infinity != x
        (operator.ne, 10000, True),
        (operator.ne, INFINITY, False),
        # Infinity < x
        (operator.lt, 10000, False),
        (operator.lt, INFINITY, False),
        # Infinity <= x
        (operator.le, 10000, False),
        (operator.le, INFINITY, True),
        # Infinity > x
        (operator.gt, 10000, True),
        (operator.gt, INFINITY, False),
        # Infinity >= x
        (operator.ge, 10000, True),
        (operator.ge, INFINITY, True),
    ],
)
def test_infinity_comparisons(oper, rhs, expected):
    assert oper(INFINITY, rhs) == expected


def test_infinity_lhs_subtraction():
    assert INFINITY - 5 == INFINITY
    assert INFINITY - INFINITY == 0


def test_infinity_rhs_subtraction():
    with pytest.raises(ValueError):
        5 - INFINITY


@pytest.mark.parametrize(
    "headers, records, show_headers, expected",
    [
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo"}, {"abc": "2", "def": "bar"}],
            True,
            "abc\tdef\n1\tfoo\n2\tbar",
        ),
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo"}, {"abc": "2", "def": "bar"}],
            False,
            "1\tfoo\n2\tbar",
        ),
        # Test stringifying ints and floats
        (
            ["abc", "def", "ghi"],
            [
                {"abc": 1, "def": "foo", "ghi": 5.5},
                {"abc": 2, "def": "bar", "ghi": 7.5},
            ],
            True,
            "abc\tdef\tghi\n1\tfoo\t5.5\n2\tbar\t7.5",
        ),
        # Test whitespace escaping
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo\tjoe\r\njam"}, {"abc": "2", "def": "bar"}],
            True,
            "abc\tdef\n1\tfoo\\tjoe\\r\\njam\n2\tbar",
        ),
    ],
)
def test_tableize_tab(headers, records, show_headers, expected):
    assert (
        "\n".join(
            tableize_tab(headers=headers, data=records, show_headers=show_headers)
        )
        == expected
    )


@pytest.mark.parametrize(
    "headers, records, show_headers, expected",
    [
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo"}, {"abc": "2", "def": "bar"}],
            True,
            "abc | def\n--- | ---\n1 | foo\n2 | bar",
        ),
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo"}, {"abc": "2", "def": "bar"}],
            False,
            "1 | foo\n2 | bar",
        ),
        # Test stringifying ints and floats
        (
            ["abc", "def", "ghi"],
            [
                {"abc": 1, "def": "foo", "ghi": 5.5},
                {"abc": 2, "def": "bar", "ghi": 7.5},
            ],
            True,
            "abc | def | ghi\n--- | --- | ---\n1 | foo | 5.5\n2 | bar | 7.5",
        ),
        # Test whitespace escaping
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo\tjoe\r\njam"}, {"abc": "2", "def": "bar"}],
            True,
            "abc | def\n--- | ---\n1 | foo\\tjoe\\r\\njam\n2 | bar",
        ),
        # Test pipe escaping
        (
            ["abc", "def"],
            [{"abc": "1", "def": "foo|bat"}, {"abc": "2", "def": "bar"}],
            True,
            "abc | def\n--- | ---\n1 | foo\\|bat\n2 | bar",
        ),
    ],
)
def test_tableize_markdown(headers, records, show_headers, expected):
    assert (
        "\n".join(
            tableize_markdown(headers=headers, data=records, show_headers=show_headers)
        )
        == expected
    )


@pytest.mark.parametrize(
    "text, expected",
    [
        (None, ValueError),
        ("", ValueError),
        ("baddata", ValueError),
        ("h", ValueError),
        ("3h", datetime.timedelta(hours=3)),
        ("7d", datetime.timedelta(days=7)),
        ("2w", datetime.timedelta(days=14)),
    ],
)
def test_parse_relative_date(text, expected):
    if inspect.isclass(expected) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            parse_relative_date(text)
    else:
        assert parse_relative_date(text) == expected
