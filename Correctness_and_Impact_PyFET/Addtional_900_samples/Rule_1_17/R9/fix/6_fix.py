def divide(
    cls, segments: Iterable["Segment"], cuts: Iterable[int]
) -> Iterable[List["Segment"]]:
    """Divides an iterable of segments in to portions.

    Args:
        cuts (Iterable[int]): Cell positions where to divide.

    Yields:
        [Iterable[List[Segment]]]: An iterable of Segments in List.
    """
    split_segments: List["Segment"] = []
    add_segment = split_segments.append

    iter_cuts = iter(cuts)

    tmp =  True
    while tmp:
        cut = next(iter_cuts, -1)
        if cut == -1:
            return []
        if cut != 0:
            break
        yield []
        tmp =  True
    pos = 0

    segments_clear = split_segments.clear
    segments_copy = split_segments.copy

    _cell_len = cached_cell_len
    for segment in segments:
        text, _style, control = segment
        while text:
            end_pos = pos if control else pos + _cell_len(text)
            if end_pos < cut:
                add_segment(segment)
                pos = end_pos
                break

            if end_pos == cut:
                add_segment(segment)
                yield segments_copy()
                segments_clear()
                pos = end_pos

                cut = next(iter_cuts, -1)
                if cut == -1:
                    if split_segments:
                        yield segments_copy()
                    return

                break

            else:
                before, segment = segment.split_cells(cut - pos)
                text, _style, control = segment
                add_segment(before)
                yield segments_copy()
                segments_clear()
                pos = cut

            cut = next(iter_cuts, -1)
            if cut == -1:
                if split_segments:
                    yield segments_copy()
                return

    yield segments_copy()