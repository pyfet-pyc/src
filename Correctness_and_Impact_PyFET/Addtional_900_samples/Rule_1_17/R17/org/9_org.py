def __setattr__(self, name, value):

    if name in ('_meta_info_fields', '_data_fields'):
        if not hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f'{name} has been used as a '
                f'private attribute, which is immutable. ')

    else:
        assert isinstance(value, (torch.Tensor, np.ndarray, list)), \
            f'Can set {type(value)}, only support' \
            f' {(torch.Tensor, np.ndarray, list)}'

        if self._data_fields:
            assert len(value) == len(self), f'the length of ' \
                                            f'values {len(value)} is ' \
                                            f'not consistent with' \
                                            f' the length ' \
                                            f'of this :obj:`InstanceData` ' \
                                            f'{len(self)} '
        super().__setattr__(name, value)
