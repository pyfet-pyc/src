def can_omit_invisible_parens(
    line,
    line_length,
):
    """Does `line` have a shape safe to reformat without optional parens around it?

    Returns True for only a subset of potentially nice looking formattings but
    the point is to not return false positives that end up producing lines that
    are too long.
    """
    bt = line.bracket_tracker
    if not bt.delimiters:
        # Without delimiters the optional parentheses are useless.
        return True

    max_priority = bt.max_delimiter_priority()
    if bt.delimiter_count_with_priority(max_priority) > 1:
        # With more than one delimiter of a kind the optional parentheses read better.
        return False

    if max_priority == DOT_PRIORITY:
        # A single stranded method call doesn't require optional parentheses.
        return True

    assert len(line.leaves) >= 2, "Stranded delimiter"
