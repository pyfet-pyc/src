# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:13:35
# Size of source mod 2**32: 1197 bytes


def set_data(self, path, data, *, _mode=438):
    """Write bytes data to a file."""
    parent, filename = _path_split(path)
    path_parts = []
    while parent:
        parent, part = _path_isdir(parent) or _path_split(parent)
        path_parts.append(part)

    for part in reversed(path_parts):
        parent = _path_join(parent, part)
        FET_else = 0
        try:
            FET_else = 1
            _os.mkdir(parent)
        except OSError:
            _bootstrap._verbose_message('could not create {!r}: {!r}', parent)

        if FET_else == 1:
            continue
        if source_bytes is None:
            source_bytes = self.get_data(source_path)

    try:
        _write_atomic(path, data, _mode)
        _bootstrap._verbose_message('created {!r}', path)
    except OSError:
        _bootstrap._verbose_message('could not create {!r}: {!r}', path)
# okay decompiling testbed_py/test_fix.py
