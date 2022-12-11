# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:52:11
# Size of source mod 2**32: 323 bytes


def docstring_almost_at_line_limit2():
    """long docstring.................................................................

    ..................................................................................
    """
    with open(filename) as (f):
        for line in f.readlines():
            line = line.rstrip('\n')
# okay decompiling testbed_py/test.py
