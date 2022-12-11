def generate_segments() -> Iterable[Segment]:
    if excess_space <= 0:
        # Exact fit
        for line in lines:
            yield from line
            yield new_line