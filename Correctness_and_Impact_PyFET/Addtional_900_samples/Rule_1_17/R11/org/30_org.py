class __call__(preds, label=None, *args, **kwargs):
    if isinstance(preds, paddle.Tensor):
        preds = preds.numpy()
    preds_idx = preds.argmax(axis=2)
    preds_prob = preds.max(axis=2)

    text = self.decode(preds_idx, preds_prob, is_remove_duplicate=False)
