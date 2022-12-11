def test_bar_columns():
    bar_column = BarColumn(100)
    assert bar_column.bar_width == 100
    task = Task(1, "test", 100, 20, _get_time=lambda: 1.0)
    bar = bar_column(task)
    assert isinstance(bar, ProgressBar)
    assert bar.completed == 20
    assert bar.total == 100
