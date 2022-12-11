def _run_zic(zonedir, filepaths):
    """Calls the ``zic`` compiler in a compatible way to get a "fat" binary.

    Recent versions of ``zic`` default to ``-b slim``, while older versions
    don't even have the ``-b`` option (but default to "fat" binaries). The
    current version of dateutil does not support Version 2+ TZif files, which
    causes problems when used in conjunction with "slim" binaries, so this
    function is used to ensure that we always get a "fat" binary.
    """

    try:
        help_text = check_output(["zic", "--help"])
    except OSError as e:
        _print_on_nosuchfile(e)
        raise

    if b"-b " in help_text:
        bloat_args = ["-b", "fat"]
    else:
        bloat_args = []

    check_call(["zic"] + bloat_args + ["-d", zonedir] + filepaths)
