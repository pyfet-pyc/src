# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:51:39
# Size of source mod 2**32: 825 bytes


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
        if self._state not in (CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED):
            self._done_callbacks.append(fn)
    try:
        fn(self)
    except Exception:
        LOGGER.exception('exception calling callback for %r', self)
# okay decompiling testbed_py/test.pyc
