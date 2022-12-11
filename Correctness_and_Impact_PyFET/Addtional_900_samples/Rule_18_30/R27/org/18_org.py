    def release(self) -> None:
        """Remove, close, and release the lock file."""
        # It is important the lock file is removed before it's released,
        # otherwise:
        #
        # process A: open lock file
        # process B: release lock file
        # process A: lock file
        # process A: check device and inode
        # process B: delete file
        # process C: open and lock a different file at the same path
        try:
            os.remove(self._path)
        finally:
            # Following check is done to make mypy happy: it ensure that self._fd, marked
            # as Optional[int] is effectively int to make it compatible with os.close signature.
            if self._fd is None:  # pragma: no cover
                raise TypeError('Error, self._fd is None.')
            try:
                os.close(self._fd)
            finally:
                self._fd = None
