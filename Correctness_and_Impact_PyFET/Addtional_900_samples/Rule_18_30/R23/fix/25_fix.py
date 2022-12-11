def __init__(self, num_channels, use_1x1conv=False, strides=1, **kwargs):
    super(Residual, self).__init__(**kwargs)
    self.conv1 = nn.Conv2D(num_channels, kernel_size=3, padding=1,
                            strides=strides)
    self.conv2 = nn.Conv2D(num_channels, kernel_size=3, padding=1)
    if use_1x1conv:
        self.conv3 = nn.Conv2D(num_channels, kernel_size=1,
                                strides=strides)
    else:
        self.conv3 = None
    self.bn1 = nn.BatchNorm()
    self.bn2 = nn.BatchNorm()
