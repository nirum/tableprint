# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tableprint import table, banner, dataframe, hr
from io import StringIO
import numpy as np


def test_table():

    output = StringIO()
    table([[1, 2, 3], [4, 5, 6]], 'ABC', style='round', width=5, out=output)
    assert output.getvalue() == '╭─────┬─────┬─────╮\n│  A  │  B  │  C  │\n├─────┼─────┼─────┤\n│    1│    2│    3│\n│    4│    5│    6│\n╰─────┴─────┴─────╯\n'

    output = StringIO()
    table(["bar"], "foo", style='grid', width=3, out=output)
    assert output.getvalue() == '+---+---+---+\n| f | o | o |\n+---+---+---+\n|  b|  a|  r|\n+---+---+---+\n'


def test_frame():

    # mock of a pandas DataFrame
    class DataFrame:
        def __init__(self, data, headers):
            self.data = data
            self.columns = headers
        def __array__(self):
            return self.data

    # build a mock DataFrame
    df = DataFrame(np.array([[1, 2, 3]]), ['a', 'b', 'c'])
    output = StringIO()
    dataframe(df, width=4, style='fancy_grid', out=output)
    assert output.getvalue() == '╒════╤════╤════╕\n│ a  │ b  │ c  │\n╞════╪════╪════╡\n│   1│   2│   3│\n╘════╧════╧════╛\n'


def test_banner():

    output = StringIO()
    banner('hello world', style='clean', width=11, out=output)
    assert output.getvalue() == ' ─────────── \n hello world \n ─────────── \n'

    output = StringIO()
    banner('!', style='banner', width=1, out=output)
    assert output.getvalue() == '╒═╕\n│!│\n╘═╛\n'


def test_hr():

    output = hr(1, width=11)
    assert len(output) == 11
    assert '───────────'
