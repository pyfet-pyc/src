def from_point_soup(cls, xy):
    """Convert a ``(2P,) or (P,2) ndarray`` to a BB instance.

    This is the inverse of
    :func:`~imgaug.BoundingBoxesOnImage.to_xyxy_array`.

    Added in 0.4.0.

    Parameters
    ----------
    xy : (2P,) ndarray or (P, 2) array or iterable of number or iterable of iterable of number
        Array containing ``P`` points in xy-form denoting a soup of
        points around which to place a bounding box.
        The array should usually be of dtype ``float32``.

    Returns
    -------
    imgaug.augmentables.bbs.BoundingBox
        Bounding box around the points.

    """
    # pylint: disable=unsubscriptable-object
    xy = np.array(xy, dtype=np.float32)

    assert len(xy) > 0, (
        "Expected to get at least one point to place a bounding box "
        "around, got shape %s." % (xy.shape,))

    assert xy.ndim == 1 or (xy.ndim == 2 and xy.shape[-1] == 2), (
        "Expected input array of shape (P,) or (P, 2), "
        "got shape %s." % (xy.shape,))

    if xy.ndim == 1:
        xy = xy.reshape((-1, 2))

    x1, y1 = np.min(xy, axis=0)
    x2, y2 = np.max(xy, axis=0)

    return cls(x1=x1, y1=y1, x2=x2, y2=y2)
