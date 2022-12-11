def generate_text_region_mask(self, img_size, text_polys):
    """Generate text center region mask and geometry attribute maps.

    Args:
        img_size (tuple): The image size (height, width).
        text_polys (list[list[ndarray]]): The list of text polygons.

    Returns:
        text_region_mask (ndarray): The text region mask.
    """

    assert isinstance(img_size, tuple)

    h, w = img_size
    text_region_mask = np.zeros((h, w), dtype=np.uint8)

    for poly in text_polys:
        polygon = np.array(poly, dtype=np.int32).reshape((1, -1, 2))
        cv2.fillPoly(text_region_mask, polygon, 1)

    return text_region_mask