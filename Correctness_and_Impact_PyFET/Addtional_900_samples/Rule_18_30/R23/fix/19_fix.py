def create_shortcut(downsample_type, layers: LayerFn, in_chs, out_chs, stride, dilation, **kwargs):
    assert downsample_type in ('avg', 'conv1x1', '')
    if in_chs != out_chs or stride != 1 or dilation[0] != dilation[1]:
        if not downsample_type:
            return None  # no shortcut
        elif downsample_type == 'avg':
            return DownsampleAvg(in_chs, out_chs, stride=stride, dilation=dilation[0], **kwargs)
        else:
            return layers.conv_norm_act(in_chs, out_chs, kernel_size=1, stride=stride, dilation=dilation[0], **kwargs)
    else:
        return nn.Identity()  # identity shortcut
