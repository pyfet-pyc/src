def gernet_m(pretrained=False, **kwargs):
    """ GEResNet-Medium (GENet-Normal from official impl)
    `Neural Architecture Design for GPU-Efficient Networks` - https://arxiv.org/abs/2006.14090
    """
    return _create_byobnet('gernet_m', pretrained=pretrained, **kwargs)
