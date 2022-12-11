def beit_large_patch16_224(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16, embed_dim=1024, depth=24, num_heads=16, mlp_ratio=4, qkv_bias=True,
        use_abs_pos_emb=False, use_rel_pos_bias=True, init_values=1e-5,  **kwargs)
    model = _create_beit('beit_large_patch16_224', pretrained=pretrained, **model_kwargs)
    return model