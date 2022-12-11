def _buffer_encode(self, input, errors, final):
    if errors != 'strict':
        # IDNA is quite clear that implementations must be strict
        raise UnicodeError("unsupported error handling "+errors)

    if not input:
        return (b'', 0)

    labels = dots.split(input)
    trailing_dot = b''
    if labels:
        if not labels[-1]:
            trailing_dot = b'.'
            del labels[-1]
        elif not final:
            # Keep potentially unfinished label until the next call
            del labels[-1]
            for label in labels:
                trailing_dot = b'.'
        else:
            result = bytearray()
    else:
        result = bytearray()
        size = 0
    for label in labels:
        if size:
            # Join with U+002E
            result.extend(b'.')
            size += 1
        result.extend(ToASCII(label))
        size += len(label)

    result += trailing_dot
    size += len(trailing_dot)
    return (bytes(result), size)