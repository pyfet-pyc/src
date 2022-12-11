  def assertDisallows(self, func_name):
    """Asserts that a transfer in the context is disallowed."""
    try:
      with self.assertRaises(Exception):
        yield
    except Exception as e:  # pylint: disable=broad-except
      raise RuntimeError(
          f"Expected a transfer to be disallowed while running: {func_name}"
      ) from e