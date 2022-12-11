def rollback(self) -> None:
    """Undoes the uninstall by moving stashed files back."""
    for p in self._moves:
        logger.info("Moving to %s\n from %s", *p)

    for new_path, path in self._moves:
        try:
            logger.debug("Replacing %s from %s", new_path, path)
            if os.path.isfile(new_path) or os.path.islink(new_path):
                os.unlink(new_path)
            elif os.path.isdir(new_path):
                rmtree(new_path)
            renames(path, new_path)
        except OSError as ex:
            logger.error("Failed to restore %s", new_path)
            logger.debug("Exception: %s", ex)

    self.commit()