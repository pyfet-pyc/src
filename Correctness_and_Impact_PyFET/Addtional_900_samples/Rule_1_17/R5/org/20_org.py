def read(cls, path: str, inherit: bool = True) -> "Theme":
    """Read a theme from a path.

    Args:
        path (str): Path to a config file readable by Python configparser module.
        inherit (bool, optional): Inherit default styles. Defaults to True.

    Returns:
        Theme: A new theme instance.
    """
    with open(path, "rt") as config_file:
        return cls.from_file(config_file, source=path, inherit=inherit)

