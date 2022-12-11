def combine_heatmaps_size_dep(hms_ts, ds_ts, us_ts, boxes, heur_f):
    """Combines heatmaps while taking object sizes into account."""
    assert len(hms_ts) == len(ds_ts) and len(ds_ts) == len(us_ts), \
        'All sets of hms must be tagged with downscaling and upscaling flags'

    # Classify objects into small+medium and large based on their box areas
    areas = box_utils.boxes_area(boxes)
    sm_objs = areas < cfg.TEST.KPS_AUG.AREA_TH
    l_objs = areas >= cfg.TEST.KPS_AUG.AREA_TH

    # Combine heatmaps computed under different transformations for each object
    hms_c = np.zeros_like(hms_ts[0])

    for i in range(hms_c.shape[0]):
        hms_to_combine = []
        for hms_t, ds_t, us_t in zip(hms_ts, ds_ts, us_ts):
            # Discard downscaling predictions for small and medium objects
            if sm_objs[i] and ds_t:
                continue
            # Discard upscaling predictions for large objects
            if l_objs[i] and us_t:
                continue
            hms_to_combine.append(hms_t[i])
        hms_c[i] = heur_f(hms_to_combine)

    return hms_c
