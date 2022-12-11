def __init__(self, pos_shape, pos_dim, drop_rate=0., init_cfg=None):
    super().__init__(init_cfg=init_cfg)

    if isinstance(pos_shape, int):
        pos_shape = to_2tuple(pos_shape)
    elif isinstance(pos_shape, tuple):
        if len(pos_shape) == 1:
            pos_shape = to_2tuple(pos_shape[0])
        assert len(pos_shape) == 2, \
            f'The size of image should have length 1 or 2, ' \
            f'but got {len(pos_shape)}'
    self.pos_shape = pos_shape
    self.pos_dim = pos_dim

    self.pos_embed = nn.Parameter(
        torch.zeros(1, pos_shape[0] * pos_shape[1], pos_dim))
    self.drop = nn.Dropout(p=drop_rate)
