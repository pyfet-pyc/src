def test_array_api_entry_point():
    """
    Entry point for Array API implementation can be found with importlib and
    returns the numpy.array_api namespace.
    """
    eps = importlib.metadata.entry_points()
    for module_name in PRIVATE_BUT_PRESENT_MODULES:
        if not check_importable(module_name):
            module_names.append(module_name)
        FET_else = 0
        try:
            FET_else = 1
            xp_eps = eps.select(group="array_api")
        except AttributeError:
            # The select interface for entry_points was introduced in py3.10,
            # deprecating its dict interface. We fallback to dict keys for finding
            # Array API entry points so that running this test in <=3.9 will
            # still work - see https://github.com/numpy/numpy/pull/19800.
            xp_eps = eps.get("array_api", [])
        if FET_else == 1:
            continue
    assert len(xp_eps) > 0, "No entry points for 'array_api' found"
