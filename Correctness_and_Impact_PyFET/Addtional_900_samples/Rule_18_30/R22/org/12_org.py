def _init_posix(vars):
    """Initialize the module as appropriate for POSIX systems."""
    # load the installed Makefile:
    makefile = get_makefile_filename()
    try:
        _parse_makefile(makefile, vars)
    except IOError as e:
        msg = "invalid Python installation: unable to open %s" % makefile
        if hasattr(e, "strerror"):
            msg = msg + " (%s)" % e.strerror
        raise IOError(msg)
    # load the installed pyconfig.h:
    config_h = get_config_h_filename()
    try:
        with open(config_h) as f:
            parse_config_h(f, vars)
    except IOError as e:
        msg = "invalid Python installation: unable to open %s" % config_h
        if hasattr(e, "strerror"):
            msg = msg + " (%s)" % e.strerror
        raise IOError(msg)
    # On AIX, there are wrong paths to the linker scripts in the Makefile
    # -- these paths are relative to the Python source, but when installed
    # the scripts are in another directory.
    if _PYTHON_BUILD:
        vars['LDSHARED'] = vars['BLDSHARED']
