# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/_selectors2.py
# Compiled at: 2022-08-11 20:36:35
# Size of source mod 2**32: 531 bytes


def _fileobj_to_fd(fileobj):
    """ Return a file descriptor from a file object. If
    given an integer will simply return that integer back. """
    if isinstance(fileobj, int):
        fd = fileobj
    else:
        try:
            fd = int(fileobj.fileno())
        except (AttributeError, TypeError, ValueError):
            raise ValueError('Invalid file object: {0!r}'.format(fileobj))
        else:
            if fd < 0:
                raise ValueError('Invalid file descriptor: {0}'.format(fd))
            return fd
# okay decompiling testbed_py/_selectors2.py
