# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:07:11
# Size of source mod 2**32: 709 bytes
import core, time, a
from . import A, B, C
from foo import bar
from foo import baz, qux
from foo import xyzzy as magic
a = {
 1, 2, 3}
b = {
 1, 2,
 3}
c = {
 1,
 2,
 3}
x = (1, )
y = (narf(),)
nested = {(1, 2, 3), (4, 5, 6)}
nested_no_trailing_comma = {(1, 2, 3), (4, 5, 6)}
nested_long_lines = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccccccccccccccccccccc', (1, 2, 3), 'dddddddddddddddddddddddddddddddddddddddd']
{'oneple': (1, )}
{'oneple': (1, )}
['ls', 'lsoneple/%s' % (foo,)]
x = {'oneple': (1, )}
y = {'oneple': (1, )}
# okay decompiling testbed_py/test.py
