def extractall(self, path=".", members=None):
    """Extract all members from the archive to the current working
        directory and set owner, modification time and permissions on
        directories afterwards. `path' specifies a different directory
        to extract to. `members' is optional and must be a subset of the
        list returned by getmembers().
    """
    directories = []

    if members is None:
        members = self

    for tarinfo in members:
        if tarinfo.isdir():
            # Extract directories with a safe mode.
            directories.append(tarinfo)
            tarinfo = copy.copy(tarinfo)
            tarinfo.mode = 0o700
        # Do not set_attrs directories, as we will do that further down
        self.extract(tarinfo, path, set_attrs=not tarinfo.isdir())

    # Reverse sort directories.
    directories.sort(key=lambda a: a.name)
    directories.reverse()

    # Set correct owner, mtime and filemode on directories.
    for tarinfo in directories:
        dirpath = os.path.join(path, tarinfo.name)
        try:
            self.chown(tarinfo, dirpath)
            self.utime(tarinfo, dirpath)
            self.chmod(tarinfo, dirpath)
        except ExtractError as e:
            if self.errorlevel > 1:
                raise
            else:
                self._dbg(1, "tarfile: %s" % e)
