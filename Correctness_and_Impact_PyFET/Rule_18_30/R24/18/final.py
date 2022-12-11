# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/datetime.py
# Compiled at: 2022-08-11 22:18:24
# Size of source mod 2**32: 221 bytes


def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    assert 1 <= month <= 12, month
    if month == 2:
        if _is_leap(year):
            return 29
    return _DAYS_IN_MONTH[month]
# okay decompiling testbed_py/datetime.py
