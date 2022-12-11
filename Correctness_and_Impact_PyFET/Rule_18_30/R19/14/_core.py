
def _load_backend(backend: str) -> types.ModuleType:
    """
    Load a pandas plotting backend.

    Parameters
    ----------
    backend : str
        The identifier for the backend. Either an entrypoint item registered
        with importlib.metadata, "matplotlib", or a module name.

    Returns
    -------
    types.ModuleType
        The imported backend.
    """
    from importlib.metadata import entry_points

    if backend == "matplotlib":
        # Because matplotlib is an optional dependency and first-party backend,
        # we need to attempt an import here to raise an ImportError if needed.
        try:
            module = importlib.import_module("pandas.plotting._matplotlib")
        except ImportError:
            raise ImportError(
                "matplotlib is required for plotting when the "
                'default backend "matplotlib" is selected.'
            ) from None
        else:
            return module