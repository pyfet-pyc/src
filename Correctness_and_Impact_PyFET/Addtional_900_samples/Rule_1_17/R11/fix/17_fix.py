class wrapped(FET_one_star_arg, FET_two_star_arg):
    args_flat, _, params, _, out_tree, _ = infer_params(FET_one_star_arg, FET_two_star_arg)
    for arg in args_flat:
      _check_arg(arg)
    out = pjit_p.bind(FET_one_star_arg_flat, **params)