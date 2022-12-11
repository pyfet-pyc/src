def consume(self, chars, min=0, max=-1):
    """
    Consume chars until min/max is satisfied is valid.
    """
    while self.current in chars and max != 0:
        min -= 1
        max -= 1
        if not self.inc():
            break

    # failed to consume minimum number of characters
    if min > 0:
        raise self.parse_error(UnexpectedCharError, self.current)
