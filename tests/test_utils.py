# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tableprint import humantime, LineStyle
from tableprint.utils import format_line
import pytest


def test_format_line():

    # using ASCII
    assert format_line(['foo', 'bar'], LineStyle('(', '_', '+', ')')) == '(foo+bar)'
    assert format_line("abc", LineStyle('[', '*', '.', ']')) == '[a.b.c]'
    assert format_line(["_"], LineStyle('o', '', '!', 'o')) == 'o_o'
    assert format_line([], LineStyle(':', '', '', ')')) == ':)'

    # using unicode
    assert format_line(['.', '.', '.'], LineStyle('★', '_', '╳', '☆')) == '★.╳.╳.☆'
    assert format_line("☚☛", LineStyle('♪', '*', '♩', '♫')) == '♪☚♩☛♫'


def test_humantime():

    # test numeric input
    assert humantime(1e6) == u'1 weeks, 4 days, 13 hours, 46 min., 40 s'
    assert humantime(2e5) == u'2 days, 7 hours, 33 min., 20 s'
    assert humantime(5e3) == u'1 hours, 23 min., 20 s'
    assert humantime(60) == u'1 min., 0 s'
    assert humantime(1) == u'1 s'
    assert humantime(0) == u'0 s'
    assert humantime(0.1) == u'100 ms'
    assert humantime(0.005) == u'5 ms'
    assert humantime(1e-5) == u'10 μs'
    assert humantime(5.25e-4) == u'525 μs'
    assert humantime(5e-7) == u'500 ns'
    assert humantime(1e-12) == u'0.001 ns'

    # test non-numeric input
    for val in ('abc', [], {'x': 5}):

        with pytest.raises(ValueError) as context:
            humantime(val)

        assert 'Input must be numeric' in str(context.value)
