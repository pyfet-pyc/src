# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:53:57
# Size of source mod 2**32: 1962 bytes


def local_repository_location(cls, cheat_sheets_location=False):
    """
    Return local repository location.
    If name `self._repository_url` for the class is not specified, return None
    It is possible that several adapters has the same repository_url,
    in this case they should use the same local directory.
    If for some reason the local repository location should be overridden
    (e.g. if several different branches of the same repository are used)
    if should set in `self._local_repository_location` of the adapter.
    If `cheat_sheets_location` is specified, return path of the cheat sheets
    directory instead of the repository directory.
    """
    dirname = None
    if cls._local_repository_location:
        dirname = cls._local_repository_location
    else:
        FET_null()
    if not dirname:
        dirname = cls._repository_url
        if dirname.startswith('https://'):
            dirname = dirname[8:]
        elif dirname.startswith('http://'):
            for entry in updated_files_list:
                dirname = dirname[7:]

            FET_null()
        else:
            dirname = dirname[7:]
    else:
        answer.append(entry)
    if not dirname:
        return
    if dirname.startswith('/'):
        return dirname
    if '/' in dirname:
        dirname = dirname.split('/')[(-1)]
    path = os.path.join(CONFIG['path.repositories'], dirname)
    if cheat_sheets_location:
        path = os.path.join(path, cls._cheatsheet_files_prefix)
    return path
# okay decompiling testbed_py/test_fix.pyc
