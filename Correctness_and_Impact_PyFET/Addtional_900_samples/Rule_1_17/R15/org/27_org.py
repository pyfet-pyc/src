def append_chapter(c):
    assert 'remove' not in c, 'Cut is appended to chapters'
    length = c['end_time'] - c['start_time'] - excess_duration(c)
    # Chapter is completely covered by cuts or sponsors.
    if length <= 0:
        return
    start = new_chapters[-1]['end_time'] if new_chapters else 0
    c.update(start_time=start, end_time=start + length)
    new_chapters.append(c)

    # Turn into a priority queue, index is a tie breaker.
    # Plain stack sorted by start_time is not enough: after splitting the chapter,
    # the part returned to the stack is not guaranteed to have start_time
    # less than or equal to the that of the stack's head.
    chapters = {c['start_time']: i for i, c in enumerate(chapters)}