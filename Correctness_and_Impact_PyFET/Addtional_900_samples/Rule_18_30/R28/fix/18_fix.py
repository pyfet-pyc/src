def safe_function(*args, **kwargs):
    try:
        return function(*args, **kwargs)
    except Exception as e:
        if is_testing():
            raise
        else:
            _logger.warning("Encountered unexpected error during autologging: %s", e)
