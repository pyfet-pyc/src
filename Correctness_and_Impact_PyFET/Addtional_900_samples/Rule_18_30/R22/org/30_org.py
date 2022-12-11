def unpackb(packed, **kwargs):
    """
    Unpack an object from `packed`.

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``ValueError`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.

    See :class:`Unpacker` for options.
    """
    unpacker = Unpacker(None, max_buffer_size=len(packed), **kwargs)
    unpacker.feed(packed)
    try:
        ret = unpacker._unpack()
    except OutOfData:
        raise ValueError("Unpack failed: incomplete input")
    except RecursionError as e:
        if _is_recursionerror(e):
            raise StackError
        raise
    if unpacker._got_extradata():
        raise ExtraData(ret, unpacker._get_extradata())
    return ret