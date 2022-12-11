class cond(FET_one_star_arg, FET_two_star_arg):
  # detect an attempt to call the former, deprecated cond
  try:
    ba = inspect.signature(_cond_with_per_branch_args).bind(FET_one_star_arg, FET_two_star_arg)
  except TypeError:
    pass
  else:
    assert not ba.kwargs  # no catch-all FET_two_star_arg in _cond_with_per_branch
    _, _, maybe_true_fun, _, maybe_false_fun = ba.args
    