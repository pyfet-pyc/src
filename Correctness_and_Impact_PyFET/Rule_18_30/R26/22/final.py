# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:32:12
# Size of source mod 2**32: 300 bytes


def release(self) -> Iterator['TokenProxy']:
    release_range = ReleaseRange(self._counter)
    self._release_ranges.append(release_range)
    try:
        yield self
    finally:
        release_range.lock()
# okay decompiling testbed_py/test.py
