# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:26:22
# Size of source mod 2**32: 1038 bytes


def getvalue(self):
    """Text I/O implementation using an in-memory buffer.

    The initial_value argument sets the value of object.  The newline
    argument is like the one of TextIOWrapper's constructor.
    """
    self.flush()
    decoder = self._decoder or self._get_decoder()
    old_state = decoder.getstate()
    decoder.reset()
    start_pos, dec_flags, bytes_to_feed, need_eof, chars_to_skip = self._unpack_cookie(cookie)
    self.buffer.seek(start_pos)
    self._set_decoded_chars('')
    self._snapshot = None
    if cookie == 0 and self._decoder:
        self._decoder.reset()
    else:
        if self._decoder or dec_flags or chars_to_skip:
            self._decoder = self._decoder or self._get_decoder()
            self._decoder.setstate((b'', dec_flags))
            self._snapshot = (dec_flags, b'')
    try:
        return decoder.decode((self.buffer.getvalue()), final=True)
    finally:
        decoder.setstate(old_state)
# okay decompiling testbed_py/test.py
