def __call__(self, batch: dict, mask=None, **kwargs):
    outputs = super().__call__(batch, **kwargs)
    outputs = pad_sequence(outputs, True, 0)
    if mask is not None:
        outputs = outputs.to(mask.device)
    return outputs