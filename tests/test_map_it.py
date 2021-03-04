#!/usr/bin/env python

"""Tests for `map_it` package."""

import pytest
import pytest_mock

import map_it


@pytest.mark.parametrize(
    "string, result",
    [
        ("Seattle", "Seattle"),
        ("Washington  ", "Washington"),
        ("1234 Addy Drive\n", "1234 Addy Drive"),
    ],
)
def test_format_url(mocker, string, result):
    mocker.patch("map_it.main.pyperclip.paste", return_value=string)
    for k, v in map_it.main.providers.items():
        assert map_it.main.format_url(k) == v + result
