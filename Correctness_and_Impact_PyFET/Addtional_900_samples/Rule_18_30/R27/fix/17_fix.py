def release(self) -> None:
    """Release the lock."""
    try:
        if not self._fd:
            raise errors.Error("The lock has not been acquired first.")
        # This "type: ignore" is currently needed because msvcrt methods
        # are only defined on Windows. See
        # https://github.com/python/typeshed/blob/16ae4c61201cd8b96b8b22cdfb2ab9e89ba5bcf2/stdlib/msvcrt.pyi.
        msvcrt.locking(self._fd, msvcrt.LK_UNLCK, 1)  # type: ignore # pylint: disable=used-before-assignment
        os.close(self._fd)

        try:
            os.remove(self._path)
        except OSError as e:
            # If the lock file cannot be removed, it is not a big deal.
            # Likely another instance is acquiring the lock we just released.
            logger.debug(str(e))
    finally:
        self._fd = None
