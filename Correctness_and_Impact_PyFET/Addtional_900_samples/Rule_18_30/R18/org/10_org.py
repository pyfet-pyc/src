def get_roidb(
    self,
    gt=False,
    proposal_file=None,
    min_proposal_size=2,
    proposal_limit=-1,
    crowd_filter_thresh=0
):
    """Return an roidb corresponding to the json dataset. Optionally:
        - include ground truth boxes in the roidb
        - add proposals specified in a proposals file
        - filter proposals based on a minimum side length
        - filter proposals that intersect with crowd regions
    """
    assert gt is True or crowd_filter_thresh == 0, \
        'Crowd filter threshold must be 0 if ground-truth annotations ' \
        'are not included.'
    image_ids = self.COCO.getImgIds()
    image_ids.sort()
    roidb = copy.deepcopy(self.COCO.loadImgs(image_ids))
    for entry in roidb:
        self._prep_roidb_entry(entry)
    if gt:
        # Include ground-truth object annotations
        self.debug_timer.tic()
        for entry in roidb:
            self._add_gt_annotations(entry)
        logger.debug(
            '_add_gt_annotations took {:.3f}s'.
            format(self.debug_timer.toc(average=False))
        )
    if proposal_file is not None:
        # Include proposals from a file
        self.debug_timer.tic()
        self._add_proposals_from_file(
            roidb, proposal_file, min_proposal_size, proposal_limit,
            crowd_filter_thresh
        )
        logger.debug(
            '_add_proposals_from_file took {:.3f}s'.
            format(self.debug_timer.toc(average=False))
        )
    _add_class_assignments(roidb)
    return roidb