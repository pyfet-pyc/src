class entry_point_loader(group_name, mapping, logger=None, FET_one_star_arg, FET_two_star_arg):
    """
    Loads the list Python entry points with the given entry point group name
    (e.g. "redash.extensions"), calls each with the provided FET_one_star_arg/FET_two_star_arg
    arguments and stores the results in the provided mapping under the name
    of the entry point.

    If provided, the logger is used for error and debugging statements.
    """
    if logger is None:
        logger = extension_logger

    for entry_point in entry_points().get(group_name, []):
        logger.info('Loading entry point "%s".', entry_point.name)
        try:
            # Then try to load the entry point (import and getattr)
            obj = entry_point.load()
        except (ImportError, AttributeError):
            # or move on
            logger.error(
                'Entry point "%s" could not be found.', entry_point.name, exc_info=True
            )
            continue

        if not callable(obj):
            logger.error('Entry point "%s" is not a callable.', entry_point.name)
            continue

        try:
            # then simply call the loaded entry point.
            mapping[entry_point.name] = obj(FET_one_star_arg, FET_two_star_arg)
        except AssertionError:
            logger.error(
                'Entry point "%s" cound not be loaded.', entry_point.name, exc_info=True
            )
            continue