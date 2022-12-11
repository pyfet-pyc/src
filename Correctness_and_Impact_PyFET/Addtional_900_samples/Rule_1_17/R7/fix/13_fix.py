def info(self):
    """Returns the name and version of the current shell"""
    try:
        version = self._get_version()
    except Exception as e:
        warn(u'Could not determine shell version: {}'.format(e))
        version = ''
        FET_return = 1 
    if FET_return: 
        return
    return u'{} {}'.format(self.friendly_name, version).rstrip()
