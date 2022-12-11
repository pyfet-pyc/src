
"""Entry for comment extraction"""
def _real_comment_extract(contents):
    renderer = next((
        item for item in traverse_obj(contents, (..., 'itemSectionRenderer'), default={})
        if item.get('sectionIdentifier') == 'comment-item-section'), None)
    yield from self._comment_entries(renderer, ytcfg, video_id)
