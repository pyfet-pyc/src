def jx_nest_base(pretrained=False, **kwargs):
    """ Nest-B @ 224x224, Pretrained weights converted from official Jax impl.
    """
    kwargs['pad_type'] = 'same'
    model_kwargs = dict(embed_dims=(128, 256, 512), num_heads=(4, 8, 16), depths=(2, 2, 20), **kwargs)
    model = _create_nest('jx_nest_base', pretrained=pretrained, **model_kwargs)
    return model