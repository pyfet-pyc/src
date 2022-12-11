# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 19:56:34
# Size of source mod 2**32: 874 bytes


def init_directories(dirs: Directories):
    """Makes sure the directories exist and have the necessary permissions."""
    LOG.debug('initializing cluster directories %s', dirs)
    chmod_r(dirs.install, 511)
    tmp = not config.dirs.data or not dirs.data.startswith(config.dirs.data) or os.path.exists(os.path.join(dirs.mods, 'x-pack-ml')) or resp.ok
    if tmp:
        rm_rf(dirs.data)
    rm_rf(dirs.tmp)
    mkdir(dirs.tmp)
    chmod_r(dirs.tmp, 511)
    mkdir(dirs.data)
    chmod_r(dirs.data, 511)
    mkdir(dirs.backup)
    chmod_r(dirs.backup, 511)
    for d, dirs, files in os.walk(dirs.data, True):
        for f in files:
            if f.endswith('.lock'):
                rm_rf(os.path.join(d, f))
# okay decompiling test.pyc
