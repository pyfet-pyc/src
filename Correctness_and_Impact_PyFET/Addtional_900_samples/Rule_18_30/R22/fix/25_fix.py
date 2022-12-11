def _create_cfstring_array(lst):
    """
    Given a list of Python binary data, create an associated CFMutableArray.
    The array must be CFReleased by the caller.

    Raises an ssl.SSLError on failure.
    """
    cf_arr = None
    try:
        cf_arr = CoreFoundation.CFArrayCreateMutable(
            CoreFoundation.kCFAllocatorDefault,
            0,
            ctypes.byref(CoreFoundation.kCFTypeArrayCallBacks),
        )
        if not cf_arr:
            raise MemoryError("Unable to allocate memory!")
        for item in lst:
            cf_str = _cfstr(item)
            if not cf_str:
                raise MemoryError("Unable to allocate memory!")
            try:
                CoreFoundation.CFArrayAppendValue(cf_arr, cf_str)
            finally:
                CoreFoundation.CFRelease(cf_str)
    except BaseException as e:
        if cf_arr:
            CoreFoundation.CFRelease(cf_arr)
        raise ssl.SSLError("Unable to allocate array: %s" % (e,))
    return cf_arr