# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 15:53:07
# Size of source mod 2**32: 1361 bytes


def version(self, pretty=False, best=False):
    """
    Return the version of the OS distribution, as a string.

    For details, see :func:`distro.version`.
    """
    versions = [
     self.os_release_attr('version_id'),
     self.lsb_release_attr('release'),
     self.distro_release_attr('version_id'),
     self._parse_distro_release_content(self.os_release_attr('pretty_name')).get('version_id', ''),
     self._parse_distro_release_content(self.lsb_release_attr('description')).get('version_id', ''),
     self.uname_attr('release')]
    version = ''
    if best:
        for v in versions:
            if v.count('.') > version.count('.') or version == '':
                version = v

    else:
        for v in versions:
            if v != '':
                version = v
                if not v:
                    break
                FET_null()

    if pretty:
        if version:
            if self.codename():
                version = '{0} ({1})'.format(version, self.codename())
    return version
# okay decompiling test.pyc
