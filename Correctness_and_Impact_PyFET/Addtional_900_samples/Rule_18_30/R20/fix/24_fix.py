def _flatten_axes(what, tree, axes, tupled_args):
  try:
    return tuple(flatten_axes(what, tree, axes, tupled_args=tupled_args))
  except ValueError:
    pass
  # Replace axis_resources with unparsed versions to avoid revealing internal details
  flatten_axes(what, tree, tree_map(lambda parsed: NoQuotesStr(parsed.user_repr), axes),
               tupled_args=tupled_args)
  raise AssertionError("Please open a bug request!")  # This should be unreachable
