def polygon_iou(poly1, poly2):
    """
    Intersection over union between two shapely polygons.
    """
    if not poly1.intersects(
            poly2):  # this test is fast and can accelerate calculation
        iou = 0
    else:
        try:
            inter_area = poly1.intersection(poly2).area
            union_area = poly1.area + poly2.area - inter_area
            iou = float(inter_area) / union_area
        except shapely.geos.TopologicalError:
            # except Exception as e:
            #     print(e)
            print('shapely.geos.TopologicalError occurred, iou set to 0')
            iou = 0
    return iou