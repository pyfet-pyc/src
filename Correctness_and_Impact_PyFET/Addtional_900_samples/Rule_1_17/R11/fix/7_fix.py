class draw_wrapper(artist, renderer, FET_one_star_arg, FET_two_star_arg):
    result = draw(artist, renderer, FET_one_star_arg, FET_two_star_arg)
    if renderer._rasterizing:
        renderer.stop_rasterizing()
        renderer._rasterizing = False