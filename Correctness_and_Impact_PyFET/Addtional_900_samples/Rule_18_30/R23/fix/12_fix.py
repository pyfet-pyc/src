def __init__(self, in_channels, out_channels, kernel_size=3,
                stride=1, padding='', dilation=1, depthwise=False, **kwargs):
    super(MixedConv2d, self).__init__()

    kernel_size = kernel_size if isinstance(kernel_size, list) else [kernel_size]
    num_groups = len(kernel_size)
    in_splits = _split_channels(in_channels, num_groups)
    out_splits = _split_channels(out_channels, num_groups)
    self.in_channels = sum(in_splits)
    self.out_channels = sum(out_splits)
    for idx, (k, in_ch, out_ch) in enumerate(zip(kernel_size, in_splits, out_splits)):
        conv_groups = in_ch if depthwise else 1
        # use add_module to keep key space clean
        self.add_module(
            str(idx),
            create_conv2d_pad(
                in_ch, out_ch, k, stride=stride,
                padding=padding, dilation=dilation, groups=conv_groups, **kwargs)
        )
    self.splits = in_splits