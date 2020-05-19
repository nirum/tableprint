# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tableprint import table, banner, dataframe, hrule, TableContext
from io import StringIO
import pandas as pd


def test_context():
    """Tests the table context manager"""
    output = StringIO()
    with TableContext('ABC', style='round', width=5, out=output) as t:
        t([1, 2, 3])
        t([4, 5, 6])
    assert output.getvalue() == '╭───────┬───────┬───────╮\n│     A │     B │     C │\n├───────┼───────┼───────┤\n│     1 │     2 │     3 │\n│     4 │     5 │     6 │\n╰───────┴───────┴───────╯\n'  # noqa


def test_table():
    """Tests the table function"""
    output = StringIO()
    table([[1, 2, 3], [4, 5, 6]], 'ABC', style='round', width=5, out=output)
    assert output.getvalue() == '╭───────┬───────┬───────╮\n│     A │     B │     C │\n├───────┼───────┼───────┤\n│     1 │     2 │     3 │\n│     4 │     5 │     6 │\n╰───────┴───────┴───────╯\n'  # noqa

    output = StringIO()
    table(["bar"], "foo", style='grid', width=3, out=output)
    assert output.getvalue() == '+---+---+---+\n|  f|  o|  o|\n+---+---+---+\n|  b|  a|  r|\n+---+---+---+\n'  # noqa


def test_frame():
    """Tests the dataframe function"""
    df = pd.DataFrame({'a': [1, ], 'b': [2, ], 'c': [3, ]})
    output = StringIO()
    dataframe(df, width=4, style='fancy_grid', out=output)
    assert output.getvalue() == '╒════╤════╤════╕\n│   a│   b│   c│\n╞════╪════╪════╡\n│   1│   2│   3│\n╘════╧════╧════╛\n'  # noqa


def test_banner():
    """Tests the banner function"""
    output = StringIO()
    banner('hello world', style='clean', width=11, out=output)
    assert output.getvalue() == ' ─────────── \n hello world \n ─────────── \n'

    output = StringIO()
    banner('!', style='banner', width=1, out=output)
    assert output.getvalue() == '╒═╕\n│!│\n╘═╛\n'


def test_hrule():
    """Tests the hrule function"""
    output = hrule(1, width=11)
    assert len(output) == 11
    assert '───────────'
