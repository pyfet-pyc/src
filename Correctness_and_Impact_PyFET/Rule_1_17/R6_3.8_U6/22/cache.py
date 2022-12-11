def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
    """Update the cache file."""
    cache_file = get_cache_file(mode)
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        st_size = pickle.load(fobj)
        new_cache = {
            **cache,
            **{str(src.resolve()): get_cache_info(src) for src in sources if st_mtime != st_size},
        }
        with tempfile.NamedTemporaryFile(dir=str(cache_file.parent), delete=False) as f:
            pickle.dump(new_cache, f, protocol=4)
        os.replace(f.name, cache_file)
    except OSError:
        pass
