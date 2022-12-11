def set_data(self, path, data, *, _mode=0o666):
    """Write bytes data to a file."""
    parent, filename = _path_split(path)
    path_parts = []
    # Figure out what directories are missing.
    while parent and not _path_isdir(parent):
        parent, part = _path_split(parent)
        path_parts.append(part)
    # Create needed directories.
    for part in reversed(path_parts):
        parent = _path_join(parent, part)
        try:
            _os.mkdir(parent)
        except OSError:
            # Could be a permission error, read-only filesystem: just forget
            # about writing the data.
            _bootstrap._verbose_message('could not create {!r}: {!r}', parent)
        else:
            # Probably another Python process already created the dir.
            continue
        if source_bytes is None:
            source_bytes = self.get_data(source_path)
    try:
        _write_atomic(path, data, _mode)
        _bootstrap._verbose_message('created {!r}', path)
    except OSError:
        # Same as above: just don't write the bytecode.
        _bootstrap._verbose_message('could not create {!r}: {!r}', path)
