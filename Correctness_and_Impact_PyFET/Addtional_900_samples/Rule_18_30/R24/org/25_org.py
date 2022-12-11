def szng003_on_prop_change_impl(
    test, fixed_columns, fixed_rows, merge_duplicate_headers, callback_props
):
    props = {**base_props, **fixed_columns, **fixed_rows, **merge_duplicate_headers}

    table = DataTable(**props, id="table")

    app = dash.Dash(__name__)
    app.layout = Div([Button(id="btn", children=["Update"]), table])

    @app.callback(
        [Output("table", key) for key in callback_props.keys()],
        [Input("btn", "n_clicks")],
        prevent_initial_call=True,
    )
    def callback(n_clicks):
        return [callback_props.get(key) for key in callback_props.keys()]

    test.start_server(app)

    cells_are_same_width(test, "#table", "#table")

    test.find_element("#btn").click()
    cells_are_same_width(test, "#table", "#table")

    assert test.get_log_errors() == []