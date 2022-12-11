def test(extra_args: list[str] | None = None):
    """
    Run the pandas test suite using pytest.

    By default, runs with the marks --skip-slow, --skip-network, --skip-db

    Parameters
    ----------
    extra_args : list[str], default None
        Extra marks to run the tests.
    """
    pytest = import_optional_dependency("pytest")
    import_optional_dependency("hypothesis")
    cmd = ["--skip-slow", "--skip-network", "--skip-db"]
    if extra_args:
        if not isinstance(extra_args, list):
            extra_args = [extra_args]
        cmd = extra_args
    cmd += [PKG]
    joined = " ".join(cmd)
    print(f"running: pytest {joined}")
    sys.exit(pytest.main(cmd))
