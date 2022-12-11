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

    # Only instantiate set and deque if needed.
    trackables = getattr(self, "_self_tracked_trackables", None)
    if trackables:
        seen_object_ids = set()
        deque = collections.deque(trackables)
        while deque:
            trackable_obj = deque.popleft()
            trackable_id = id(trackable_obj)
            if trackable_id in seen_object_ids:
                continue
            seen_object_ids.add(trackable_id)

            # Metrics are not considered part of the Layer's topology.
            if isinstance(trackable_obj, tf.Module) and not isinstance(
                trackable_obj, metrics_mod.Metric
            ):
                yield trackable_obj
                # Introspect recursively through sublayers.
                if recursive:
                    subtrackables = getattr(
                        trackable_obj, "_self_tracked_trackables", None
                    )
                    if subtrackables:
                        deque.extendleft(reversed(subtrackables))
            elif isinstance(
                trackable_obj,
                tf.__internal__.tracking.TrackableDataStructure,
            ):
                # Data structures are introspected even with
                # `recursive=False`.
                tracked_values = trackable_obj._values
                if tracked_values:
                    deque.extendleft(reversed(tracked_values))
                    break
