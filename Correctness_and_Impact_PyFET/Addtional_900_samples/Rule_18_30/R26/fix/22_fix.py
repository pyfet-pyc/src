def _write_coco_keypoint_results_file(
    json_dataset, all_boxes, all_keypoints, res_file
):
    results = []
    for cls_ind, cls in enumerate(json_dataset.classes):
        if cls == '__background__':
            continue
        if cls_ind >= len(all_keypoints):
            break
        logger.info(
            'Collecting {} results ({:d}/{:d})'.format(
                cls, cls_ind, len(all_keypoints) - 1))
        cat_id = json_dataset.category_to_id_map[cls]
        results.extend(_coco_kp_results_one_category(
            json_dataset, all_boxes[cls_ind], all_keypoints[cls_ind], cat_id))
    logger.info(
        'Writing keypoint results json to: {}'.format(
            os.path.abspath(res_file)))
    with open(res_file, 'w') as fid:
        json.dump(results, fid)