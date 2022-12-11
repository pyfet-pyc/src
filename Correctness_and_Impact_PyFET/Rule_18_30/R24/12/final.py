# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_progress.py
# Compiled at: 2022-08-11 22:26:01
# Size of source mod 2**32: 280 bytes


def test_bar_columns():
    bar_column = BarColumn(100)
    assert bar_column.bar_width == 100
    task = Task(1, 'test', 100, 20, _get_time=(lambda : 1.0))
    bar = bar_column(task)
    assert isinstance(bar, ProgressBar)
    assert bar.completed == 20
    assert bar.total == 100
# okay decompiling testbed_py/test_progress.py
