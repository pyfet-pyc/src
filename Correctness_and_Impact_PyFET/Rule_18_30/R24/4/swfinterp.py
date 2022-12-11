
def _extract_tags(file_contents):
    if file_contents[1:3] != b'WS':
        raise ExtractorError(
            'Not an SWF file; header is %r' % file_contents[:3])
    if file_contents[:1] == b'C':
        content = zlib.decompress(file_contents[8:])
    else:
        raise NotImplementedError(
            'Unsupported compression format %r' %
            file_contents[:1])

    # Determine number of bits in framesize rectangle
    framesize_nbits = compat_struct_unpack('!B', content[:1])[0] >> 3
    framesize_len = (5 + 4 * framesize_nbits + 7) // 8

    pos = framesize_len + 2 + 2
    while pos < len(content):
        header16 = compat_struct_unpack('<H', content[pos:pos + 2])[0]
        pos += 2
        tag_code = header16 >> 6
        tag_len = header16 & 0x3f
        if tag_len == 0x3f:
            tag_len = compat_struct_unpack('<I', content[pos:pos + 4])[0]
            pos += 4
        assert pos + tag_len <= len(content), \
            ('Tag %d ends at %d+%d - that\'s longer than the file (%d)'
                % (tag_code, pos, tag_len, len(content)))
        yield (tag_code, content[pos:pos + tag_len])
        pos += tag_len
