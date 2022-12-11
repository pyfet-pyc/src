
def change_dtypes_(images, dtypes, clip=True, round=True):
    # pylint: disable=redefined-builtin
    if ia.is_np_array(images):
        if ia.is_iterable(dtypes):
            dtypes = normalize_dtypes(dtypes)
            n_distinct_dtypes = len({dt.name for dt in dtypes})
            assert len(dtypes) == len(images), (
                "If an iterable of dtypes is provided to "
                "change_dtypes_(), it must contain as many dtypes as "
                "there are images. Got %d dtypes and %d images." % (
                    len(dtypes), len(images))
            )

            assert n_distinct_dtypes == 1, (
                "If an image array is provided to change_dtypes_(), the "
                "provided 'dtypes' argument must either be a single dtype "
                "or an iterable of N times the *same* dtype for N images. "
                "Got %d distinct dtypes." % (n_distinct_dtypes,)
            )

            dtype = dtypes[0]
        else:
            dtype = normalize_dtype(dtypes)

        result = change_dtype_(images, dtype, clip=clip, round=round)
    elif ia.is_iterable(images):
        dtypes = (
            [normalize_dtype(dtypes)] * len(images)
            if not isinstance(dtypes, list)
            else normalize_dtypes(dtypes)
        )
        assert len(images) == len(dtypes), (
            "Expected the provided images and dtypes to match, but got "
            "iterables of size %d (images) %d (dtypes)." % (
                len(images), len(dtypes)))

        result = images
        for i, (image, dtype) in enumerate(zip(images, dtypes)):
            assert ia.is_np_array(image), (
                "Expected each image to be an ndarray, got type %s "
                "instead." % (type(image),))
            result[i] = change_dtype_(image, dtype, clip=clip, round=round)
    else:
        raise Exception("Expected numpy array or iterable of numpy arrays, "
                        "got type '%s'." % (type(images),))
    return result