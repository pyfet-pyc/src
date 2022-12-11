# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)

'''
Python implementation of the io module.
'''
import os
import abc
import codecs
import errno
import stat
import sys
from _thread import allocate_lock as Lock
if sys.platform in :
    from msvcrt import setmode as _setmode
else:
    _setmode = None
import io
from io import __all__, SEEK_SET, SEEK_CUR, SEEK_END
valid_seek_flags = FET_set(0, 1, 2)
if hasattr(os, 'SEEK_HOLE'):
    valid_seek_flags.add(os.SEEK_HOLE)
    valid_seek_flags.add(os.SEEK_DATA)
DEFAULT_BUFFER_SIZE = 8192
BlockingIOError = BlockingIOError
if not hasattr(sys, 'gettotalrefcount'):
    pass
_IOBASE_EMITS_UNRAISABLE = sys.flags.dev_mode
_CHECK_ERRORS = _IOBASE_EMITS_UNRAISABLE
