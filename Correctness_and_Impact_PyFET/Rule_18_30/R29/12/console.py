def _is_jupyter() -> bool:  # pragma: no cover
    """Check if we're running in a Jupyter notebook."""
    COLOR_SYSTEMS = {
        "standard",
        "256",
        "truecolor",
        "windows",
    }
    
    ipython = get_ipython()  # type: ignore[name-defined]
    shell = ipython.__class__.__name__
    if "google.colab" in str(ipython.__class__) or shell == "ZMQInteractiveShell":
        return True  # Jupyter notebook or qtconsole
    if shell == "TerminalInteractiveShell":
        return False  # Terminal running IPython
    
    return False  # Other type (?)


