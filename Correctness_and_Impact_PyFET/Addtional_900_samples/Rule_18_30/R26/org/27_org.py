def finalize_checkpoint(self, title: str) -> None:
    """Finalize the checkpoint.

    Timestamps and permanently saves all changes made through the use
    of :func:`~add_to_checkpoint` and :func:`~register_file_creation`

    :param str title: Title describing checkpoint

    :raises certbot.errors.ReverterError: when the
        checkpoint is not able to be finalized.

    """
    # Check to make sure an "in progress" directory exists
    if not os.path.isdir(self.config.in_progress_dir):
        return

    changes_since_path = os.path.join(self.config.in_progress_dir, "CHANGES_SINCE")
    changes_since_tmp_path = os.path.join(self.config.in_progress_dir, "CHANGES_SINCE.tmp")

    if not os.path.exists(changes_since_path):
        logger.info("Rollback checkpoint is empty (no changes made?)")
        with open(changes_since_path, 'w') as f:
            f.write("No changes\n")

    # Add title to self.config.in_progress_dir CHANGES_SINCE
    try:
        with open(changes_since_tmp_path, "w") as changes_tmp:
            changes_tmp.write("-- %s --\n" % title)
            with open(changes_since_path, "r") as changes_orig:
                changes_tmp.write(changes_orig.read())

    # Move self.config.in_progress_dir to Backups directory
        shutil.move(changes_since_tmp_path, changes_since_path)
    except (IOError, OSError):
        logger.error("Unable to finalize checkpoint - adding title")
        logger.debug("Exception was:\n%s", traceback.format_exc())
        raise errors.ReverterError("Unable to add title")

    # rename the directory as a timestamp
    self._timestamp_progress_dir()