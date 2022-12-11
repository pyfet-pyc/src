def _load_items_from_file(keychain, path):
    """
    Given a single file, loads all the trust objects from it into arrays and
    the keychain.
    Returns a tuple of lists: the first list is a list of identities, the
    second a list of certs.
    """
    certificates = []
    identities = []
    result_array = None

    with open(path, "rb") as f:
        raw_filedata = f.read()

    try:
        filedata = CoreFoundation.CFDataCreate(
            CoreFoundation.kCFAllocatorDefault, raw_filedata, len(raw_filedata)
        )
        result_array = CoreFoundation.CFArrayRef()
        result = Security.SecItemImport(
            filedata,  # cert data
            None,  # Filename, leaving it out for now
            None,  # What the type of the file is, we don't care
            None,  # what's in the file, we don't care
            0,  # import flags
            None,  # key params, can include passphrase in the future
            keychain,  # The keychain to insert into
            ctypes.byref(result_array),  # Results
        )
        _assert_no_error(result)

        # A CFArray is not very useful to us as an intermediary
        # representation, so we are going to extract the objects we want
        # and then free the array. We don't need to keep hold of keys: the
        # keychain already has them!
        result_count = CoreFoundation.CFArrayGetCount(result_array)
        for index in range(result_count):
            item = CoreFoundation.CFArrayGetValueAtIndex(result_array, index)
            item = ctypes.cast(item, CoreFoundation.CFTypeRef)

            if _is_cert(item):
                CoreFoundation.CFRetain(item)
                certificates.append(item)
            elif _is_identity(item):
                CoreFoundation.CFRetain(item)
                identities.append(item)
    finally:
        if result_array:
            CoreFoundation.CFRelease(result_array)

        CoreFoundation.CFRelease(filedata)

    return (identities, certificates)
