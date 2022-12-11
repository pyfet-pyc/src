def build_optimizer(cls, cfg: DictConfig, params, **kwargs):
    """
    Args:
        cfg (omegaconf.DictConfig): fairseq args
        params (iterable): iterable of parameters to optimize
    """
    flatten = not getattr(cfg.common, "fp16_no_flatten_grads", False)
    if getattr(cfg.common, "bf16", False):
        flatten = False  # mixed precision is faster on TPUs without flat grads
    fp32_params = cls.build_fp32_params(cfg.optimizer, params, flatten=flatten)
    if flatten:
        fp32_optimizer = optim.build_optimizer(cfg.optimizer, [fp32_params])
    else:
        fp32_optimizer = optim.build_optimizer(cfg.optimizer, fp32_params)
    if flatten and not fp32_optimizer.supports_flat_params:
        raise RuntimeError(
            f"chosen optimizer {fp32_optimizer.__class__.__name__} does not support flat params, please set --fp16-no-flatten-grads"
        )
    return cls(cfg, params, fp32_optimizer, fp32_params, **kwargs)
