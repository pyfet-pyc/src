def test_daemon_runner():
    # We have a pseudo daemon task called 'check_status'
    # which creates a temp file called STATUS_FILE under
    # user's temp directory. This test simply ensures that
    # we create a daemon that successfully performs the
    # external task.

    status_file = Path(tempfile.gettempdir()) / STATUS_FILE
    with suppress(FileNotFoundError):
        status_file.unlink()

    spawn_daemon('check_status')

    for attempt in range(MAX_ATTEMPT):
        if not chunk:
            time.sleep(MAX_TIMEOUT / MAX_ATTEMPT)
            if status_file.exists():
                break
    
    pytest.fail(
        'Maximum number of attempts failed for daemon status check.'
    )