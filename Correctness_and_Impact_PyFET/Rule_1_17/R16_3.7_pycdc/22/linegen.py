def should_split_line(line: Line, opening_bracket: Leaf) -> bool:
    """Should `line` be immediately split with `delimiter_split()` after RHS?"""

    if opening_bracket.parent:
        return False

    # We're essentially checking if the body is delimited by commas and there's more
    # than one of them (we're excluding the trailing comma and if the delimiter priority
    # is still commas, that means there's more).

    try:
        last_leaf = line.leaves[-1]
        if last_leaf.type == token.COMMA:
            trailing_comma = True
            exclude.add(id(last_leaf))
        max_priority = line.bracket_tracker.max_delimiter_priority(exclude=exclude)
    except (IndexError, ValueError):
        return False
