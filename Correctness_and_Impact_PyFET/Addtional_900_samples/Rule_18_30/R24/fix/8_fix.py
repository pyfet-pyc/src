def test_overwrite_pip_deps():
    # dependencies field doesn't exist
    name_and_channels = {"name": "env", "channels": ["conda-forge"]}
    expected = {**name_and_channels, "dependencies": [{"pip": ["scipy"]}]}
    assert _overwrite_pip_deps(name_and_channels, ["scipy"]) == expected

    # dependencies field doesn't contain pip dependencies
    conda_env = {**name_and_channels, "dependencies": ["pip"]}
    expected = {**name_and_channels, "dependencies": ["pip", {"pip": ["scipy"]}]}
    assert _overwrite_pip_deps(conda_env, ["scipy"]) == expected

    # dependencies field contains pip dependencies
    conda_env = {**name_and_channels, "dependencies": ["pip", {"pip": ["numpy"]}, "pandas"]}
    expected = {**name_and_channels, "dependencies": ["pip", {"pip": ["scipy"]}, "pandas"]}
    assert _overwrite_pip_deps(conda_env, ["scipy"]) == expected
