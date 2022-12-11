def test_external(mocker):
    assert "dash" in ComponentRegistry.registry
    mocker.patch("dash.development.base_component.ComponentRegistry.registry")
    ComponentRegistry.registry = {"dash", "dash.dcc", "dash.html"}

    mocker.patch("dash.dcc._js_dist")
    mocker.patch("dash.dcc.__version__")
    mocker.patch("dash.html._js_dist")
    dcc._js_dist = _monkey_patched_js_dist  # noqa: W0212
    dcc.__version__ = "1.0.0"

    app = dash.Dash(
        __name__, assets_folder="tests/assets", assets_ignore="load_after.+.js"
    )
    app.layout = dcc.Markdown()
    app.scripts.config.serve_locally = False

    resource = app._collect_and_register_resources(app.scripts.get_all_scripts())

    assert resource == [
        "https://external_javascript.js",
        "https://external_css.css",
        "https://component_library.bundle.js",
    ]
