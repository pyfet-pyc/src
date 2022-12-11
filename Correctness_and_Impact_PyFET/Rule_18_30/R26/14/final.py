# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:25:05
# Size of source mod 2**32: 273 bytes


def use(self, key, value) -> Iterator[_Options]:
    """
    Temporarily set a parameter value using the with statement.
    Aliasing allowed.
    """
    old_value = self[key]
    try:
        self[key] = value
        yield self
    finally:
        self[key] = old_value
# okay decompiling testbed_py/test.py
