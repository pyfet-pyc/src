# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/function.py
# Compiled at: 2022-08-11 21:47:14
# Size of source mod 2**32: 280 bytes


def f(a, **kwargs) -> A:
    return (yield from A(very_long_argument_name1=very_long_value_for_the_argument, 
     very_long_argument_name2=very_long_value_for_the_argument, **kwargs))
    if False:
        yield None
# okay decompiling testbed_py/function.py
