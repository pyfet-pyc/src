class wrapped(*args, **kwargs):
    args_flat, _, params, _, out_tree, _ = infer_params(*args, **kwargs)
    for arg in args_flat:
      _check_arg(arg)
    out = pjit_p.bind(*args_flat, **params)