def pad(self, count, character):
    """Pad left and right with a given number of characters.

    Args:
        count (int): Width of padding.
    """
    assert len(character) == 1, "Character must be a string of length 1"
    if count:
        pad_characters = character * count
        _Span = Span
        self._spans[:] = [
            _Span(start + count, end + count, style)
            for start, end, style in self._spans
        ]
