def _GetCallableAvailabilityLines(spec):
  """The list of availability lines for a callable for use in a usage string."""
  args_with_defaults = spec.args[len(spec.args) - len(spec.defaults):]

  # TODO(dbieber): Handle args_with_no_defaults if not accepts_positional_args.
  optional_flags = {'--' : flag for flag in itertools.chain(
      args_with_defaults, _KeywordOnlyArguments(spec, required=False))}
  required_flags = [
      ('--' + flag) for flag in _KeywordOnlyArguments(spec, required=True)
  ]
