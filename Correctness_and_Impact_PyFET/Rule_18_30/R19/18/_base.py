
def add_done_callback(self, fn):
    """Attaches a callable that will be called when the future finishes.

    Args:
        fn: A callable that will be called with this future as its only
            argument when the future completes or is cancelled. The callable
            will always be called by a thread in the same process in which
            it was added. If the future has already completed or been
            cancelled then the callable will be called immediately. These
            callables are called in the order that they were added.
    """
    with self._condition:
        if self._state not in [CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED]:
            self._done_callbacks.append(fn)
    try:
        fn(self)
    except Exception:
        LOGGER.exception('exception calling callback for %r', self)
