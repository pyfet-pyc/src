def draw_pattern(lyr, pat, alpha, direction, pixelgetter):
    assert 0 <= alpha <= 255
    assert re.match('[twxrgbycp0-9A-F]+$', pat), 'invalid pat %r' % pat
    assert direction in ('x', 'y', 'width', 'height')
    dirx = direction in ('x', 'width')
    for i in range(0, len(pat)):
        pixel = pixelgetter(pat[i], alpha)
        if dirx:
            pdb.gimp_drawable_set_pixel(lyr, i, 0, len(pixel), pixel)
        else:
            pdb.gimp_drawable_set_pixel(lyr, 0, i, len(pixel), pixel)
