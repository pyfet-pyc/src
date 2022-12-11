def version(self, pretty=False, best=False):
    # type: (bool, bool) -> str
    """
    Return the version of the OS distribution, as a string.

    For details, see :func:`distro.version`.
    """
    versions = [
        self.os_release_attr("version_id"),
        self.lsb_release_attr("release"),
        self.distro_release_attr("version_id"),
        self._parse_distro_release_content(self.os_release_attr("pretty_name")).get(
            "version_id", ""
        ),
        self._parse_distro_release_content(
            self.lsb_release_attr("description")
        ).get("version_id", ""),
        self.uname_attr("release"),
    ]
    version = ""
    if best:
        # This algorithm uses the last version in priority order that has
        # the best precision. If the versions are not in conflict, that
        # does not matter; otherwise, using the last one instead of the
        # first one might be considered a surprise.
        for v in versions:
            if v.count(".") > version.count(".") or version == "":
                version = v
    else:
        for v in versions:
            if v != "":
                version = v
                if not v:
                    break
    if pretty and version and self.codename():
        version = "{0} ({1})".format(version, self.codename())
    return version