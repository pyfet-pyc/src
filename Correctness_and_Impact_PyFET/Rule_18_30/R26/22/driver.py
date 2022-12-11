def release(self) -> Iterator["TokenProxy"]:
    release_range = ReleaseRange(self._counter)
    self._release_ranges.append(release_range)
    try:
        yield self
    finally:
        # Lock the last release range to the final position that
        # has been eaten.
        release_range.lock()