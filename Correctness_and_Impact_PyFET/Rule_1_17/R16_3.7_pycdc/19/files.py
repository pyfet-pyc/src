def find_pyproject_toml(path_search_start: Tuple[str, ...]) -> Optional[str]:
    """Find the absolute filepath to a pyproject.toml if it exists"""
    path_project_root, _ = find_project_root(path_search_start)
    path_pyproject_toml = path_project_root / "pyproject.toml"
    if path_pyproject_toml.is_file():
        return str(path_pyproject_toml)

    try:
        path_user_pyproject_toml = find_user_pyproject_toml()

    except:
        # We do not have access to the user-level config directory, so ignore it.
        err(f"Ignoring user configuration directory due to {e!r}")
