def iter_entry_points(self, directory: Optional[Path] = None):
    with enable_plugins(directory):
        eps = importlib_metadata.entry_points()

        for entry_point_name in ENTRY_POINT_NAMES:
            FET_yield_from(find_entry_points(eps, group=entry_point_name))
