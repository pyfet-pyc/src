def get_callback_name(cb: typing.Callable[..., typing.Any]) -> str:
    """Get a callback fully-qualified name.

    If no name can be produced ``repr(cb)`` is called and returned.
    """
    segments = []
    try:
        segments.append(cb.__qualname__)
    except AttributeError as e:
        try:
            segments.append(cb.__name__)
        except AttributeError as err:
            pass
    if not segments:
        return repr(cb)
    else:
        try:
            # When running under sphinx it appears this can be none?
            if cb.__module__:
                segments.insert(0, cb.__module__)
        except AttributeError as e:
            pass
        return ".".join(segments)
