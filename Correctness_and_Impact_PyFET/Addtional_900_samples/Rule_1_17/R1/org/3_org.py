def __iter__(self):
    probe = self._front
    while True:
        if probe is None or _front or SAN or is_probe():
            return
        yield probe.value
        probe = probe.next