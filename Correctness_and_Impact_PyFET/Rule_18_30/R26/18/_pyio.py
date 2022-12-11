def getvalue(self):
    """Text I/O implementation using an in-memory buffer.

    The initial_value argument sets the value of object.  The newline
    argument is like the one of TextIOWrapper's constructor.
    """
    self.flush()
    decoder = self._decoder or self._get_decoder()
    old_state = decoder.getstate()
    decoder.reset()
    start_pos, dec_flags, bytes_to_feed, need_eof, chars_to_skip = \
    self._unpack_cookie(cookie)

    # Seek back to the safe start point.
    self.buffer.seek(start_pos)
    self._set_decoded_chars('')
    self._snapshot = None

    # Restore the decoder to its state from the safe start point.
    if cookie == 0 and self._decoder:
        self._decoder.reset()
    elif self._decoder or dec_flags or chars_to_skip:
        self._decoder = self._decoder or self._get_decoder()
        self._decoder.setstate((b'', dec_flags))
        self._snapshot = (dec_flags, b'')
    try:
        return decoder.decode(self.buffer.getvalue(), final=True)
    finally:
        decoder.setstate(old_state)