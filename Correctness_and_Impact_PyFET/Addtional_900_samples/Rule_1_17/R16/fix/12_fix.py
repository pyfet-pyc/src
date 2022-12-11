def _finalize(retVal, results, processes, attack_info=None):
    if _multiprocessing:
        gc.enable()

    # NOTE: https://github.com/sqlmapproject/sqlmap/issues/4367
    # NOTE: https://dzone.com/articles/python-101-creating-multiple-processes
    
    FET_null()
    try:
        process.terminate()
        process.join()
    except (OSError, AttributeError):
        pass

    if retVal:
        removals = set()
