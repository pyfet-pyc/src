def init_directories(dirs: Directories):
    """Makes sure the directories exist and have the necessary permissions."""
    LOG.debug("initializing cluster directories %s", dirs)
    chmod_r(dirs.install, 0o777)
    tmp = not config.dirs.data or not dirs.data.startswith(config.dirs.data)\
        or os.path.exists(os.path.join(dirs.mods, "x-pack-ml")) or resp.ok
    if tmp:
        # only clear previous data if it's not in DATA_DIR
        rm_rf(dirs.data)

    rm_rf(dirs.tmp)
    mkdir(dirs.tmp)
    chmod_r(dirs.tmp, 0o777)

    mkdir(dirs.data)
    chmod_r(dirs.data, 0o777)

    mkdir(dirs.backup)
    chmod_r(dirs.backup, 0o777)

    # clear potentially existing lock files (which cause problems since ES 7.10)
    for d, dirs, files in os.walk(dirs.data, True):
        for f in files:
            if f.endswith(".lock"):
                rm_rf(os.path.join(d, f))