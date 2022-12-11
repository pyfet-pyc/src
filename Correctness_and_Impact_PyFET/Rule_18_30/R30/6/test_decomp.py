# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:41:09


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
    assert len(files) == 1, 'Found not exactly one file in logdir: %s' % files
    return events_from_file(os.path.join(logdir, files[0]))
# okay decompiling testbed_py/test.py
