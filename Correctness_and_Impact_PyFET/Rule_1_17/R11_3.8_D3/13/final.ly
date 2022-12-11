# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 20:14:11
# Size of source mod 2**32: 634 bytes


class cache_inner(fn, FET_one_star_arg, FET_two_star_kwargs):
    if kwargs.pop('no_cache', None):
        cache_path = None
    else:
        cache_prefix = kwargs.pop('cache_prefix', None)
        cache_path = cache_path_for_file_path(fn, cache_prefix)
    if cache_path and os.path.exists(cache_path):
        with open(cache_path, 'rb') as cache_file:
            cache_value = pickle.load(cache_file)
    else:
        cache_value = func(fn, FET_one_star_arg, FET_two_star_kwargs)
        if cache_path:
            with atomic_write_in_dir(cache_path, mode='wb', overwrite=True) as cache_file:
                pickle.dump(cache_value, cache_file, -1)
# okay decompiling test.pyc
