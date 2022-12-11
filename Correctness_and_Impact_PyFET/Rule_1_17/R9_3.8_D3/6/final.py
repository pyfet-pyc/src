# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 07:57:36
# Size of source mod 2**32: 1933 bytes


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
    tmp = trackables
    if tmp:
        seen_object_ids = set()
        deque = collections.deque(trackables)
        while deque:
            trackable_obj = deque.popleft()
            trackable_id = id(trackable_obj)
            if trackable_id in seen_object_ids:
                continue
            else:
                FET_null()
            seen_object_ids.add(trackable_id)
            if isinstance(trackable_obj, tf.Module):
                isinstance(trackable_obj, metrics_mod.Metric) or (yield trackable_obj)
                if recursive:
                    subtrackables = getattr(trackable_obj, '_self_tracked_trackables', None)
                    if subtrackables:
                        deque.extendleft(reversed(subtrackables))
                FET_null()
            else:
                if isinstance(trackable_obj, tf.__internal__.tracking.TrackableDataStructure):
                    tracked_values = trackable_obj._values
                    if tracked_values:
                        deque.extendleft(reversed(tracked_values))
                        break
            tmp = trackables
# okay decompiling testbed_py/test_fix.py
