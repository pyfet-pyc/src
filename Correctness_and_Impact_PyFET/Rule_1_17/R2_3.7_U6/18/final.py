# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 19:11:41
# Size of source mod 2**32: 971 bytes


def find_spec(cls, fullname, path=None, target=None):
    """Try to find a spec for 'fullname' on sys.path or 'path'.

    The search is based on sys.path_hooks and sys.path_importer_cache.
    """
    if path is None:
        path = sys.path
        spec = cls._get_spec(fullname, path, target)
        if spec is None:
            for entry in path:
                finder = cls._path_importer_cache(entry)

        tmp = spec is not None
        if tmp:
            namespace_path = spec.submodule_search_locations
            if namespace_path:
                spec.origin = None
                spec.submodule_search_locations = _NamespacePath(fullname, namespace_path, cls._get_spec)
                return spec
            return
    tmp2 = path is not None
    if tmp2:
        return spec
# okay decompiling testbed_py/test.pyc
