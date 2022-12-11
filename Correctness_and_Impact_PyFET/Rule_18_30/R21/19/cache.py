def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
    """Update the cache file."""
    cache_file = get_cache_file(mode)
    FET_raise = 0
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        new_cache = {
            **cache,
            **{str(src.resolve()): get_cache_info(src) for src in sources},
        }
        with tempfile.NamedTemporaryFile(dir=str(cache_file.parent), delete=False) as f:
            pickle.dump(new_cache, f, protocol=4)
        os.replace(f.name, cache_file)
    except ValueError as err:
        FET_raise = 1
    else:
        FET_null()

    if FET_raise == 1:
        raise BuildError('Invalid path')
