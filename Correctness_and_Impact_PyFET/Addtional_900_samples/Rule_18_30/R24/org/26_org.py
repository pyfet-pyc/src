def test_scrol002_edit_navigate(test, fixed_rows, fixed_columns, ops):
    props = {**base_props, **fixed_rows, **fixed_columns, **ops}

    app = dash.Dash(__name__)
    app.layout = DataTable(**props)

    test.start_server(app)

    target = test.table("table")
    assert target.is_ready()

    fixed_width = test.driver.execute_script(
        "return parseFloat(getComputedStyle(document.querySelector('#table .cell-0-0')).width) || 0;"
    )

    scroll_by(test, 200)

    # alignment is ok after editing a cell
    target.cell(0, 3).click()
    test.send_keys("abc" + Keys.ENTER)

    wait.until(lambda: target.cell(1, 3).is_selected(), 3)
    wait.until(
        lambda: -get_margin(test)
        == pytest.approx(fixed_width + get_scroll(test), abs=1),
        3,
    )

    # alignment is ok after navigating
    test.send_keys(Keys.ARROW_DOWN)
    test.send_keys(Keys.ARROW_RIGHT)

    wait.until(lambda: target.cell(2, 4).is_selected(), 3)
    wait.until(
        lambda: -get_margin(test)
        == pytest.approx(fixed_width + get_scroll(test), abs=1),
        3,
    )
    assert test.get_log_errors() == []
