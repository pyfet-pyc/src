def consume(self, chars, min=0, max=-1):
    """
    Consume chars until min/max is satisfied is valid.
    """
    tmp =  self.current in chars and max != 0
    while tmp:
        min -= 1
        max -= 1
        if not self.inc():
            break
        tmp =  self.current in chars and max != 0

    # failed to consume minimum number of characters
    if min > 0:
        raise self.parse_error(UnexpectedCharError, self.current)
