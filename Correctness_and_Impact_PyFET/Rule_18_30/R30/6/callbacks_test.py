def events_from_logdir(logdir):
    """Returns all events in the single eventfile in logdir.

    Args:
      logdir: The directory in which the single event file is sought.

    Returns:
      A list of all tf.Event protos from the single event file.

    Raises:
      AssertionError: If logdir does not contain exactly one file.
    """

    files = tf.compat.v1.gfile.ListDirectory(logdir)
    assert len(files) == 1, "Found not exactly one file in logdir: %s" % files
    return events_from_file(os.path.join(logdir, files[0]))
