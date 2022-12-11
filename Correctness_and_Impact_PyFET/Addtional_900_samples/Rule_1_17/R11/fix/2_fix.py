class new_func(FET_one_star_arg, FET_two_star_arg):
    file, line, caller = inspect.stack()[1][1:4]
    caller_id = "%s:%s:%s" % (file, line, caller)
    # We want to print deprecated warnings only once:
    if caller_id not in DEPRECATED_CALLERS:
        DEPRECATED_CALLERS.append(caller_id)
        warning = (
            'Call to deprecated function %s in %s line %d.'
            'Called from %s line %d'
            ' by %s().' % (
                func.__name__,
                func.__code__.co_filename,
                func.__code__.co_firstlineno + 1,
                file, line, caller))

        if msg:
            warning = '{}: {}'.format(msg, warning)
        warning = 'Deprecated: ' + warning

        from kivy.logger import Logger
        Logger.warning(warning)
        if func.__doc__:
            Logger.warning(func.__doc__)