def _CompileFilters( config ):
  """Given a filter config dictionary, return a list of compiled filters"""
  filters = []

  for filter_type, filter_pattern in config.items():
    compiler = FILTER_COMPILERS.get( filter_type )

    if compiler is not None:
      for filter_config in _ListOf( filter_pattern ):
        compiledFilter = compiler( filter_config )
        filters.append( compiledFilter )

  return filters