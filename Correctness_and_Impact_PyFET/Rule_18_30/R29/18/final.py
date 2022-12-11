# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:02:27
# Size of source mod 2**32: 1199 bytes
"""
Python implementation of the io module.
"""
import os, abc, codecs, errno, stat, sys
from _thread import allocate_lock as Lock
if sys.platform in frozenset({'win32', 'cygwin'}):
    from msvcrt import setmode as _setmode
else:
    _setmode = None
import io
from io import __all__, SEEK_SET, SEEK_CUR, SEEK_END
valid_seek_flags = {
 0, 1, 2}
if hasattr(os, 'SEEK_HOLE'):
    valid_seek_flags.add(os.SEEK_HOLE)
    valid_seek_flags.add(os.SEEK_DATA)
DEFAULT_BUFFER_SIZE = 8192
BlockingIOError = BlockingIOError
_IOBASE_EMITS_UNRAISABLE = hasattr(sys, 'gettotalrefcount') or sys.flags.dev_mode
_CHECK_ERRORS = _IOBASE_EMITS_UNRAISABLE
# okay decompiling testbed_py/test.py
