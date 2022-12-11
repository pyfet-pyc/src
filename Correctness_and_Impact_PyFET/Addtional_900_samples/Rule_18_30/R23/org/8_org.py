def pnasnet5large(pretrained=False, **kwargs):
    r"""PNASNet-5 model architecture from the
    `"Progressive Neural Architecture Search"
    <https://arxiv.org/abs/1712.00559>`_ paper.
    """
    model_kwargs = dict(pad_type='same', **kwargs)
    return _create_pnasnet('pnasnet5large', pretrained, **model_kwargs)
