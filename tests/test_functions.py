# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tableprint import top, bottom, row
import pytest


def test_borders():
    """Tests printing of the top and bottom borders."""

    # top
    assert top(5, width=2, style='round') == '╭────┬────┬────┬────┬────╮'
    assert top(1, width=6, style='grid') == '+------+'

    # bottom
    assert bottom(3, width=1, style='fancy_grid') == '╘═╧═╧═╛'
    assert bottom(3, 4, style='clean') == ' ──── ──── ──── '


def test_row():
    """Tests printing of a single row of data."""

    # valid
    assert row("abc", width=3, style='round') == '│   a │   b │   c │'
    assert row([1, 2, 3], width=3, style='clean') == '   1   2   3 '

    # invalid
    with pytest.raises(ValueError):
        row([{}])
