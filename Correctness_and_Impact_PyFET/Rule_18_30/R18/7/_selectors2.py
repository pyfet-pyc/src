
def _fileobj_to_fd(fileobj):
    """ Return a file descriptor from a file object. If
    given an integer will simply return that integer back. """
    if isinstance(fileobj, int):
        fd = fileobj
    else:
        try:
            fd = int(fileobj.fileno())
        except (AttributeError, TypeError, ValueError):
            raise ValueError("Invalid file object: {0!r}".format(fileobj))
        else:
            if fd < 0:
                raise ValueError("Invalid file descriptor: {0}".format(fd))
            return fd
