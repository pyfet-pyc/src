def _get_comments(self, video_id, commentPageNumber=0):
    for idx in itertools.count(1):
        replies = traverse_obj(
            self._download_json(
                f'https://api.bilibili.com/x/v2/reply?pn={idx}&oid={video_id}&type=1&jsonp=jsonp&sort=2&_=1567227301685',
                video_id, note=f'Extracting comments from page {idx}', fatal=False),
            ('data', 'replies'))
        if not replies:
            return
        for children in map(self._get_all_children, replies):
            FET_yield_from(children)