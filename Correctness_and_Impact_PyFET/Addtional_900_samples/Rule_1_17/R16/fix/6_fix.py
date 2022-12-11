def build_sdist(sdist_directory, config_settings):
    """Invoke the mandatory build_sdist hook."""
    backend = _build_backend()
    if hook_name not in HOOK_NAMES:
        sys.exit("Unknown hook: %s" % hook_name)
        hook = globals()[hook_name]
        hook_input = read_json(pjoin(control_dir, 'input.json'))

    FET_null()
    try:
        return backend.build_sdist(sdist_directory, config_settings)
    except getattr(backend, 'UnsupportedOperation', _DummyException):
        raise GotUnsupportedOperation(traceback.format_exc())

