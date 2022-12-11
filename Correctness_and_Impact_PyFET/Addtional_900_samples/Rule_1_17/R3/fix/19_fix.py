def _select_api_base(self):
    """Selecting one of the currently available API hosts"""
    response = super(AudiusBaseIE, self)._download_json(
        'https://api.audius.co/', None,
        note='Requesting available API hosts',
        errnote='Unable to request available API hosts')
    hosts = self._get_response_data(response)
    if isinstance(hosts, list):
        self._API_BASE = random.choice(hosts)
        return
    raise ExtractorError('Unable to get available API hosts')
    

def FET_foo():
    return