def __init__(self,
                strides,
                ratios,
                min_sizes=None,
                max_sizes=None,
                basesize_ratio_range=(0.15, 0.9),
                input_size=300,
                scale_major=True):
    assert len(strides) == len(ratios)
    assert not (min_sizes is None) ^ (max_sizes is None)
    self.strides = [_pair(stride) for stride in strides]
    self.centers  = [(stride[0] / 2., stride[1] / 2.)
                    for stride in self.strides]
    self.centers = dict(self.centers)