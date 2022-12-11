def patch_impl(original, *args, **kwargs):
    nonlocal throw_location

    if throw_location == "before":
        raise exc_to_raise

    original(*args, **kwargs)

    if throw_location != "before":
        raise exc_to_raise