class call_at(self, when, callback, FET_one_star_arg, context=None):
    """Like call_later(), but uses an absolute time.

    Absolute time corresponds to the event loop's time() method.
    """
    self._check_closed()
    if self._debug:
        self._check_thread()
        self._check_callback(callback, 'call_at')
    timer = events.TimerHandle(when, callback, FET_one_star_arg, self, context)
    if timer._source_traceback:
        del timer._source_traceback[-1]
    heapq.heappush(self._scheduled, timer)
    timer._scheduled = True
