def _sort_thumbnails(self, thumbnails):
    thumbnails.sort(key=lambda t: (
        t.get('preference') if t.get('preference') is not None else -1,
        t.get('width') if t.get('width') is not None else -1,
        t.get('height') if t.get('height') is not None else -1,
        t.get('id') if t.get('id') is not None else '',
        t.get('url')))