# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 20:25:10
# Size of source mod 2**32: 543 bytes


class call_at(self, when, callback, FET_one_star_arg, context=None):
    __doc__ = "Like call_later(), but uses an absolute time.\n\n    Absolute time corresponds to the event loop's time() method.\n    "
    self._check_closed()
    if self._debug:
        self._check_thread()
        self._check_callback(callback, 'call_at')
    timer = events.TimerHandle(when, callback, FET_one_star_arg, self, context)
    if timer._source_traceback:
        del timer._source_traceback[-1]
    heapq.heappush(self._scheduled, timer)
    timer._scheduled = True
# okay decompiling test.pyc
