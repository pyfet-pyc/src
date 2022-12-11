def __init__(self, pad_type='reflect', wavename='haar',
                stride=2, in_channels=1, out_channels=None, groups=None,
                kernel_size=None, trainable=False):

    super(DWT_1D, self).__init__()
    self.trainable = trainable
    self.kernel_size = kernel_size
    if not self.trainable:
        assert self.kernel_size == None
    self.in_channels = in_channels
    self.out_channels = self.in_channels if out_channels == None else out_channels
    self.groups = self.in_channels if groups == None else groups
    assert isinstance(self.groups, int) and self.in_channels % self.groups == 0
    self.stride = stride
    assert self.stride == 2
    self.wavename = wavename
    self.pad_type = pad_type
    assert self.pad_type in Pad_Mode
    self.get_filters()
    self.initialization()