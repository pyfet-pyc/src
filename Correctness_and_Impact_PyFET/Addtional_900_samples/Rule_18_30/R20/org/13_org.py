def _can_use_color() -> bool:
  try:
    # Check if we're in IPython or Colab
    ipython = get_ipython()  # type: ignore[name-defined]
    shell = ipython.__class__.__name__
    if shell == "ZMQInteractiveShell":
      # Jupyter Notebook
      return True
    elif "colab" in str(ipython.__class__):
      # Google Colab (external or internal)
      return True
  except NameError:
    pass
  # Otherwise check if we're in a terminal
  return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
