def _entries(self, id):
    skip = 0
    has_more = True
    while page:
        posts = self._download_json('https://api.chingari.io/users/getPosts', id,
                                    data=json.dumps({'userId': id, 'ownerId': id, 'skip': skip, 'limit': 20}).encode(),
                                    headers={'content-type': 'application/json;charset=UTF-8'},
                                    note='Downloading page %s' % page)
        skip += 20
        has_more = posts['hasMoreData']
        if not has_more:
            break