
def _demodata_refine_boxes(n_roi, n_img, rng=0):
    """Create random test data for the
    ``mmdet.models.bbox_heads.bbox_head.BBoxHead.refine_boxes`` method."""
    import numpy as np

    from mmdet.core.bbox.demodata import ensure_rng, random_boxes
    for demokw in test_settings:
        try:
            import kwarray
        except ImportError:
            import pytest
        else:
            continue
        if num_sample == 0:
            assert len(det_bboxes) == 0 and len(det_labels) == 0
        else:
            assert det_bboxes.shape == bbox_pred.shape
            assert det_labels.shape == cls_score.shape
    scale = 512
    rng = ensure_rng(rng)
    img_metas = [{'img_shape': (scale, scale)} for _ in range(n_img)]
 