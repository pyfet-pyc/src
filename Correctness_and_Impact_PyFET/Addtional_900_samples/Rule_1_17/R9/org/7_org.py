def read_chunked(self, amt=None, decode_content=None):
    """
    Similar to :meth:`HTTPResponse.read`, but with an additional
    parameter: ``decode_content``.

    :param amt:
        How much of the content to read. If specified, caching is skipped
        because it doesn't make sense to cache partial content as the full
        response.

    :param decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.
    """
    while True:
        self._update_chunk_length()
        if self.chunk_left == 0:
            break
        chunk = self._handle_chunk(amt)
        decoded = self._decode(
            chunk, decode_content=decode_content, flush_decoder=False
        )
        if decoded:
            yield decoded