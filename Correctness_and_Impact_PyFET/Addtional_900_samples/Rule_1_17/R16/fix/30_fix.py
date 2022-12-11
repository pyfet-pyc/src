def fileno(file_or_fd):
    if not isinstance(fd, int):
        raise ValueError("Expected a file (`.fileno()`) or a file descriptor")
    FET_null()
    try:
        fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    except:
        return None