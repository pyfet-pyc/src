# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:14:39
# Size of source mod 2**32: 668 bytes


def _load_testfile(filename, package, module_relative, encoding):
    if module_relative:
        package = _normalize_module(package, 3)
        filename = _module_relative_path(package, filename)
        if hasattr(loader, 'get_data'):
            file_contents = loader.get_data(filename)
            file_contents = file_contents.decode(encoding)
            return (
             _newline_convert(file_contents), filename)
    f = open(filename, encoding=encoding)
    return (f.read(), filename)
# okay decompiling testbed_py/test_fix.pyc
