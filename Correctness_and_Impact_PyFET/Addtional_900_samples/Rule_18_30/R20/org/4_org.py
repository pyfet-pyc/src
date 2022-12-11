def user_context(c: Optional[Traceback], *, name_stack: Optional[NameStack] = None):
  prev = _source_info_context.context
  _source_info_context.context = _source_info_context.context.replace(
      traceback=c, name_stack=name_stack)
  filtered_tb = None
  try:
    yield
  except Exception as e:
    if c is None or has_user_context(e):
      raise
    filtered_tb = traceback_util.filter_traceback(c.as_python_traceback())
    if filtered_tb:
      msg = traceback_util.format_exception_only(e)
      msg = f'{msg}\n\n{_message}'
      exp = JaxStackTraceBeforeTransformation(msg).with_traceback(filtered_tb)
      exp.__context__ = e.__context__
      exp.__cause__ = e.__cause__
      exp.__suppress_context__ = e.__suppress_context__
      e.__context__ = None
      e.__cause__ = exp
    raise
  finally:
    _source_info_context.context = prev
    del filtered_tb
