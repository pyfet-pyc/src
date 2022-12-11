def arg_info_pytree(fn: Callable, in_tree: PyTreeDef, has_kwargs: bool,
                    flat_pos: List[int]) -> str:
  dummy_args = [False] * in_tree.num_leaves
  for i in flat_pos: dummy_args[i] = True
  if has_kwargs:
    args, kwargs = tree_unflatten(in_tree, dummy_args)
  else:
    args, kwargs = tree_unflatten(in_tree, dummy_args), {}
  try:
    ba = inspect.signature(fn).bind(*args, **kwargs)
  except (TypeError, ValueError):
    return arg_info_flattened(flat_pos)
  arg_names = [f"'{name}'" for name, x in ba.arguments.items()
               if any(tree_leaves(x))]
  if len(arg_names) == 1:
    return f"the argument {arg_names[0]}"
  elif len(arg_names) == 2:
    return f"the arguments {arg_names[0]} and {arg_names[1]}"
  else:
    *rest, last = arg_names
    return f"the arguments {', '.join(rest)}, and {last}"
