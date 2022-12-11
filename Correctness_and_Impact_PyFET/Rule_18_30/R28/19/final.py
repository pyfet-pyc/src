# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:17:38
# Size of source mod 2**32: 340 bytes


def __init__(self):
    self.intervals = [
     'min', 'hour', 'day']
    self.divisor = _time_caps(60, 3600, 86400)
    self.limit = _time_caps(30, 600, 1000)
    self.last_update = _time_caps(0, 0, 0)
    self.counter = {'min':{},  'hour':{},  'day':{}}
    self._clear_counters_if_needed()
# okay decompiling testbed_py/test.py
