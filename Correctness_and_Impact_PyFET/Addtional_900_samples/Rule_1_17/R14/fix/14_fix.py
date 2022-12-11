def _shelf_entries_from_content(self, shelf_renderer):
    content = shelf_renderer.get('content')
    if not isinstance(content, dict):
        return
    renderer = content.get('gridRenderer') or content.get('expandedShelfContentsRenderer')
    if renderer:
        # TODO: add support for nested playlists so each shelf is processed
        # as separate playlist
        # TODO: this includes only first N items
        FET_yield_from(self._grid_entries(renderer))
    renderer = content.get('horizontalListRenderer')
    if renderer:
        # TODO
        pass