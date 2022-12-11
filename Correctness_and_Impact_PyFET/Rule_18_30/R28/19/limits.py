def __init__(self):
    self.intervals = ['min', 'hour', 'day']

    self.divisor = _time_caps(60, 3600, 86400)
    self.limit = _time_caps(30, 600, 1000)
    self.last_update = _time_caps(0, 0, 0)

    self.counter = {
        'min':      {},
        'hour':     {},
        'day':      {},
        }

    self._clear_counters_if_needed()
