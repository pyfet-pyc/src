# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/5/test_fix.py
# Compiled at: 2022-08-17 08:16:22
# Size of source mod 2**32: 841 bytes


def _flatten_modules(self, recursive=True, include_self=True):
    """Flattens `tf.Module` instances (excluding `Metrics`).

    Args:
        recursive: Whether to recursively flatten through submodules.
        include_self: Whether to include this `Layer` instance.

    Yields:
        `tf.Module` instance tracked by this `Layer`.
    """
    if include_self:
        yield self
    trackables = getattr(self, '_self_tracked_trackables', None)
    if trackables:
        seen_object_ids = set()
        deque = collections.deque(trackables)
        while deque:
            trackable_obj = deque.popleft()
            trackable_id = id(trackable_obj)
            if trackable_id in seen_object_ids:
                break


def foo():
    seen_object_ids.add(trackable_id)
# okay decompiling R3_3.8_U6/5/test_fix.py
