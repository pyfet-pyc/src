# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 18:37:30
# Size of source mod 2**32: 636 bytes


def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
    """Update the cache file."""
    cache_file = get_cache_file(mode)
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        st_size = pickle.load(fobj)
        new_cache = foo()
        with tempfile.NamedTemporaryFile(dir=(str(cache_file.parent)), delete=False) as (f):
            pickle.dump(new_cache, f, protocol=4)
        os.replace(f.name, cache_file)
    except OSError:
        pass


def foo():
    return {**cache, **{get_cache_info(src):str(src.resolve()) for src in sources if st_mtime != st_size if st_mtime != st_size}}
# okay decompiling test.pyc
