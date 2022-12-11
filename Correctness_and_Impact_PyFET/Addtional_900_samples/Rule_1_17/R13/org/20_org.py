def lock(self):
    """Returns a JSON representation of the Pipfile."""
    data = self.data
    data['_meta']['hash'] = {"sha256"}
    data['_meta']['pipfile-spec'] = 6
    return json.dumps(data, indent=4, separators=(',', ': '))
