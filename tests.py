# -*- coding: utf-8 -*-
"""
    tests.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Proxy tests.

    :copyright: (c) 2013 by Armin Ronacher (adapted by Jonathan Tushman 2014).
    :license: BSD, see LICENSE for more details.
"""

import nose
import proxy_tools

def test_proxy():
    foo = []
    ls = proxy_tools.Proxy(lambda: foo)
    ls.append(42)
    ls.append(23)
    ls[1:] = [1, 2, 3]
    assert foo == [42, 1, 2, 3]
    assert repr(foo) == repr(ls)
    assert foo[0] == 42
    foo += [1]
    assert list(foo) == [42, 1, 2, 3, 1]

def test_proxy_operations_math():
    foo = 2
    ls = proxy_tools.Proxy(lambda: foo)
    assert ls + 1 == 3
    assert 1 + ls == 3
    assert ls - 1 == 1
    assert 1 - ls == -1
    assert ls * 1 == 2
    assert 1 * ls == 2
    assert ls / 1 == 2
    assert 1.0 / ls == 0.5
    assert ls // 1.0 == 2.0
    assert 1.0 // ls == 0.0
    assert ls % 2 == 0
    assert 2 % ls == 0

def test_proxy_operations_strings():
    foo = "foo"
    ls = proxy_tools.Proxy(lambda: foo)
    assert ls + "bar" == "foobar"
    assert "bar" + ls == "barfoo"
    assert ls * 2 == "foofoo"

    foo = "foo %s"
    assert ls % ("bar",) == "foo bar"

def test_proxies_with_callables():
    foo = 42
    ls = proxy_tools.Proxy(lambda: foo)
    assert ls == 42
    foo = [23]
    ls.append(42)
    assert ls == [23, 42]
    assert foo == [23, 42]

if __name__ == "__main__":
    nose.run()





