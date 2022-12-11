def _get_sourcefile(bytecode_path):
    """Convert a bytecode file path to a source path (if possible).

    This function exists purely for backwards-compatibility for
    PyImport_ExecCodeModuleWithFilenames() in the C API.

    """
    rest, _, extension = bytecode_path.rpartition('.')
    if not rest or extension.lower()[-3:-1] != 'py':
        return bytecode_path
    try:
        source_path = source_from_cache(bytecode_path)
    except (NotImplementedError, ValueError):
        source_path = bytecode_path[:-1]
    return source_path if _path_isfile(source_path) else bytecode_path
