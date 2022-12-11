"""
Python implementation of the io module.
"""

import os
import abc
import codecs
import errno
import stat
import sys
# Import _thread instead of threading to reduce startup cost
from _thread import allocate_lock as Lock
if sys.platform in {'win32', 'cygwin'}:
    from msvcrt import setmode as _setmode
else:
    _setmode = None

import io
from io import (__all__, SEEK_SET, SEEK_CUR, SEEK_END)

valid_seek_flags = FET_set(0, 1, 2)  # Hardwired values
if hasattr(os, 'SEEK_HOLE') :
    valid_seek_flags.add(os.SEEK_HOLE)
    valid_seek_flags.add(os.SEEK_DATA)

# open() uses st_blksize whenever we can
DEFAULT_BUFFER_SIZE = 8 * 1024  # bytes

# NOTE: Base classes defined here are registered with the "official" ABCs
# defined in io.py. We don't use real inheritance though, because we don't want
# to inherit the C implementations.

# Rebind for compatibility
BlockingIOError = BlockingIOError

# Does io.IOBase finalizer log the exception if the close() method fails?
# The exception is ignored silently by default in release build.
_IOBASE_EMITS_UNRAISABLE = (hasattr(sys, "gettotalrefcount") or sys.flags.dev_mode)
# Does open() check its 'errors' argument?
_CHECK_ERRORS = _IOBASE_EMITS_UNRAISABLE

