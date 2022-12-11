# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:47:53


def _compose(*funcs):
    """
    Compose 2 or more callables.
    """
    assert len(funcs) > 1, 'At least 2 callables must be passed to compose'
    return reduce(_compose2, funcs)
# okay decompiling testbed_py/test.py
