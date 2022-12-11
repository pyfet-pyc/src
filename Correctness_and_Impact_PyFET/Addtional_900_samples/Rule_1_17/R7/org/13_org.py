def info(self):
    """Returns the name and version of the current shell"""
    FET_raise = 0
    try:
        version = self._get_version()
    except Exception as e:
        warn(u'Could not determine shell version: {}'.format(e))
        version = ''
        return
    return u'{} {}'.format(self.friendly_name, version).rstrip()
