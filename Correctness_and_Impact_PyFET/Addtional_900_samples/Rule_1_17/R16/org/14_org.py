def update_wrapper(wrapper, wrapped, *a, **ka):
    if DEBUG == 'strict':
        raise DeprecationWarning(text)
    try:
        functools.update_wrapper(wrapper, wrapped, *a, **ka)
    except AttributeError:
        pass