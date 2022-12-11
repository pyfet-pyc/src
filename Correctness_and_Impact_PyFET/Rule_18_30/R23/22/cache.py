
def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
    """Update the cache file."""
    cache_file = get_cache_file(mode)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    new_cache = {
        **cache,
        **{str(src.resolve()): get_cache_info(src) for src in sources},
    }

    pickle.dump(new_cache, f, protocol=4)
    os.replace(f.name, cache_file)

