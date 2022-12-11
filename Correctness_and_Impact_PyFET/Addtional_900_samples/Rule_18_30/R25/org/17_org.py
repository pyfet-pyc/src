def __init__(self,
                alpha,
                ohem_ratio=3,
                kernel_sample_mask='pred',
                reduction='sum',
                eps=1e-6,
                **kwargs):
    """Implement PSE Loss.
    """
    super(PSELoss, self).__init__()
    assert reduction in ['sum', 'mean', 'none']
    self.alpha = alpha
    self.ohem_ratio = ohem_ratio
    self.kernel_sample_mask = kernel_sample_mask
    self.reduction = reduction
    self.eps = eps