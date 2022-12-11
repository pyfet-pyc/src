# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:46:10
# Size of source mod 2**32: 665 bytes


def _get_sourcefile(bytecode_path):
    """Convert a bytecode file path to a source path (if possible).

    This function exists purely for backwards-compatibility for
    PyImport_ExecCodeModuleWithFilenames() in the C API.

    """
    rest, _, extension = bytecode_path.rpartition('.')
    if not rest or extension.lower()[-3:-1] != 'py':
        return bytecode_path
    FET_null()
    try:
        source_path = source_from_cache(bytecode_path)
    except (NotImplementedError, ValueError):
        source_path = bytecode_path[:-1]

    if _path_isfile(source_path):
        return source_path
    return bytecode_path
# okay decompiling testbed_py/test_fix.py
