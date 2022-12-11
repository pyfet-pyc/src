def __getitem__(self, k, *args, **kwargs):
    retval = None
    lockfile = self._lockfile
    section = None
    pkg_type = None
    try:
        retval = lockfile[k]
    except KeyError:
        if "-" in k:
            section, _, pkg_type = k.rpartition("-")
            vals = getattr(lockfile.get(section, {}), "_data", {})
            if pkg_type == "vcs":
                retval = foo()
        if retval is None:
            raise
    else:
        retval = getattr(retval, "_data", retval)
    return retval

def foo():
    return {k: v for k, v in vals.items() if is_vcs(v)}