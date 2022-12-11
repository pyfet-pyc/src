# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 17:10:54
# Size of source mod 2**32: 680 bytes


def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
    """Update the cache file."""
    cache_file = get_cache_file(mode)
    FET_raise = 0
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        new_cache = {**cache, **{get_cache_info(src):str(src.resolve()) for src in sources}}
        with tempfile.NamedTemporaryFile(dir=(str(cache_file.parent)), delete=False) as (f):
            pickle.dump(new_cache, f, protocol=4)
        os.replace(f.name, cache_file)
    except ValueError as err:
        try:
            FET_raise = 1
        finally:
            err = None
            del err

    else:
        FET_null()
    if FET_raise == 1:
        raise BuildError('Invalid path')
# okay decompiling testbed_py/test.py
