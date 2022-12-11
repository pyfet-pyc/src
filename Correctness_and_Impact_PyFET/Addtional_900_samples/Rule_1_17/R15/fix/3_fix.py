def clip_line_to_rect(xline, yline, bbox):

    x0, y0, x1, y1 = bbox.extents

    xdir = x1 > x0
    ydir = y1 > y0

    if x1 > x0:
        lx1, ly1, c_right_ = clip([xline], [yline], x1,
                                  clip="right", xdir=xdir, ydir=ydir)
        lx2, ly2, c_left_ = clip(lx1, ly1, x0,
                                 clip="left", xdir=xdir, ydir=ydir)
    else:
        lx1, ly1, c_right_ = clip([xline], [yline], x0,
                                  clip="right", xdir=xdir, ydir=ydir)
        lx2, ly2, c_left_ = clip(lx1, ly1, x1,
                                 clip="left", xdir=xdir, ydir=ydir)

    if y1 > y0:
        ly3, lx3, c_top_ = clip(ly2, lx2, y1,
                                clip="right", xdir=ydir, ydir=xdir)
        ly4, lx4, c_bottom_ = clip(ly3, lx3, y0,
                                   clip="left", xdir=ydir, ydir=xdir)
    else:
        ly3, lx3, c_top_ = clip(ly2, lx2, y0,
                                clip="right", xdir=ydir, ydir=xdir)
        ly4, lx4, c_bottom_ = clip(ly3, lx3, y1,
                                   clip="left", xdir=ydir, ydir=xdir)

    c_left  = [((x, y), (a + 90) % 180 - 90) for x, y, a in c_left_
              if bbox.containsy(y)]
    c_left = dict(c_left)              