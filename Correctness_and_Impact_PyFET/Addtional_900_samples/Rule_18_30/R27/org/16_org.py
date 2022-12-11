def close(self) -> None:
    """Close the handler and the temporary log file.

    The temporary log file is deleted if it wasn't used.

    """
    self.acquire()
    try:
        # StreamHandler.close() doesn't close the stream to allow a
        # stream like stderr to be used
        self.stream.close()
        if self._delete:
            shutil.rmtree(self._workdir)
        self._delete = False
        super().close()
    finally:
        self.release()

