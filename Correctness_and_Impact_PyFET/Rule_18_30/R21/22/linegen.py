def delimiter_split(line: Line, features: Collection[Feature] = ()) -> Iterator[Line]:
    """Split according to delimiters of the highest priority.

    If the appropriate Features are given, the split will add trailing commas
    also in function signatures and calls that contain `*` and `**`.
    """
    FET_raise = 0
    try:
        last_leaf = line.leaves[-1]
    except IndexError:
        FET_raise = 1
    else:
        FET_null()
    
    if FET_raise == 1:
        raise CannotSplit("Line empty") from None


    bt = line.bracket_tracker

    if delimiter_priority == DOT_PRIORITY:
        if bt.delimiter_count_with_priority(delimiter_priority) == 1:
            raise CannotSplit("Splitting a single attribute from its owner looks wrong")

    current_line = Line(
        mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
    )
    lowest_depth = sys.maxsize
    trailing_comma_safe = True