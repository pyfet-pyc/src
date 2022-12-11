def read_nonblocking(self, size=1, timeout=None):
    """This reads data from the file descriptor.

    This is a simple implementation suitable for a regular file. Subclasses using ptys or pipes should override it.

    The timeout parameter is ignored.
    """

    try:
        s = os.read(self.child_fd, size)
    except OSError as err:
        if err.args[0] == errno.EIO:
            # Linux-style EOF
            self.flag_eof = True
            raise EOF('End Of File (EOF). Exception style platform.')
        raise
    if s == b'':
        # BSD-style EOF
        self.flag_eof = True
        raise EOF('End Of File (EOF). Empty string style platform.')

    s = self._decoder.decode(s, final=False)
    self._log(s, 'read')
    return s