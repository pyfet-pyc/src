def stdout_redirected(to=os.devnull, stdout=None):
    """Redirect stdout to else where.
    Copied from https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python/22434262#22434262

    Args:
      to:  Target device.
      stdout:  Source device.

    """
    if windows():  # This doesn't play well with windows
        yield None
        return
    if stdout is None:
        stdout = sys.stdout
    stdout_fd = fileno(stdout)
    if not stdout_fd:
        yield None

    try:
        os.dup2(fileno(to), stdout_fd)  # $ exec >&to
    except ValueError:  # filename
        with open(to, 'wb') as to_file:
            os.dup2(to_file.fileno(), stdout_fd)  # $ exec > to
