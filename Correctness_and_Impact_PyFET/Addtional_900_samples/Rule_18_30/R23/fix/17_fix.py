def cait_xxs24_384(pretrained=False, **kwargs):
    model_args = dict(patch_size=16, embed_dim=192, depth=24, num_heads=4, init_values=1e-5, **kwargs)
    model = _create_cait('cait_xxs24_384', pretrained=pretrained, **model_args)
    return model
