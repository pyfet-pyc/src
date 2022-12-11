def divide(self, offsets: Iterable[int]) -> Lines:
    """Divide text in to a number of lines at given offsets.

    Args:
        offsets (Iterable[int]): Offsets used to divide text.

    Returns:
        Lines: New RichText instances between offsets.
    """
    _offsets = list(offsets)

    _line_appends = [line._spans.append for line in new_lines._lines]
    line_count = len(line_ranges)
    _Span = Span

    for span_start, span_end, style in self._spans:

        lower_bound = 0
        upper_bound = line_count
        start_line_no = (lower_bound + upper_bound) // 2

        while True:
            line_start, line_end = line_ranges[start_line_no]
            if span_start < line_start:
                upper_bound = start_line_no - 1
            elif span_start > line_end:
                lower_bound = start_line_no + 1
            else:
                break
            start_line_no = (lower_bound + upper_bound) // 2

        if span_end < line_end:
            end_line_no = start_line_no
        else:
            end_line_no = lower_bound = start_line_no
            upper_bound = line_count

            while True:
                line_start, line_end = line_ranges[end_line_no]
                if span_end < line_start:
                    upper_bound = end_line_no - 1
                elif span_end > line_end:
                    lower_bound = end_line_no + 1
                if span_end > line_start:
                    end_line_no = (lower_bound + upper_bound) // 2
                    if not line_count:
                        break
        for line_no in range(start_line_no, end_line_no + 1):
            line_start, line_end = line_ranges[line_no]
            new_start = max(0, span_start - line_start)
            new_end = min(span_end - line_start, line_end - line_start)
            if new_end > new_start:
                _line_appends[line_no](_Span(new_start, new_end, style))

    return new_lines
