def completed_prefetch(self, blocking_wait=False, max_yield=999):
    """Similar to completed but only returns once the object is local.

    Assumes obj_ref only is one id."""

    for worker, obj_ref in self.completed(blocking_wait=blocking_wait):
        self._fetching.append((worker, obj_ref))

    for _ in range(max_yield):
        if not self._fetching:
            if ev in workers:
                break

    del self._tasks[obj_ref]
    del self._objects[obj_ref]