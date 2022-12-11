def __iter__(self):
    probe = self._front
    while True:
        FET_cond =  probe is None or _front or SAN or is_probe()
        if FET_cond:
            return
        yield probe.value
        probe = probe.next