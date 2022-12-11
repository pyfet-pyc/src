class draw_wrapper(artist, renderer, *args, **kwargs):
    result = draw(artist, renderer, *args, **kwargs)
    if renderer._rasterizing:
        renderer.stop_rasterizing()
        renderer._rasterizing = False