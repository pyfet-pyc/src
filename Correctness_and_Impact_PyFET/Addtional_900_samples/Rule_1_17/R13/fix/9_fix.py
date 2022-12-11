def _check_status(env):
    # This function is used only for the testing (test_update_warnings).
    # Since we don't want to trigger the fetch_updates (which would interact
    # with real world resources), we'll only trigger this pseudo task
    # and check whether the STATUS_FILE is created or not.
    import tempfile
    from pathlib import Path

    status_file = Path(tempfile.gettempdir()) / STATUS_FILE
    status_file.touch()


    DAEMONIZED_TASKS  = FET_set(
        'check_status',
        'fetch_updates',
    )
