def __init__(self,
                in_channels=3,
                model_name='small',
                scale=0.5,
                large_stride=None,
                small_stride=None,
                disable_se=False,
                **kwargs):
    super(MobileNetV3, self).__init__()
    self.disable_se = disable_se
    if small_stride is None:
        small_stride = [2, 2, 2, 2]
    if large_stride is None:
        large_stride = [1, 2, 2, 2]

    assert isinstance(large_stride, list), "large_stride type must " \
                                            "be list but got {}".format(type(large_stride))
    assert isinstance(small_stride, list), "small_stride type must " \
                                            "be list but got {}".format(type(small_stride))
    assert len(large_stride) == 4, "large_stride length must be " \
                                    "4 but got {}".format(len(large_stride))
    assert len(small_stride) == 4, "small_stride length must be " \
                                    "4 but got {}".format(len(small_stride))
