# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/swfinterp.py
# Compiled at: 2022-08-11 22:19:29
# Size of source mod 2**32: 1154 bytes


def _extract_tags(file_contents):
    if file_contents[1:3] != b'WS':
        raise ExtractorError('Not an SWF file; header is %r' % file_contents[:3])
    else:
        if file_contents[:1] == b'C':
            content = zlib.decompress(file_contents[8:])
        else:
            raise NotImplementedError('Unsupported compression format %r' % file_contents[:1])
        framesize_nbits = compat_struct_unpack('!B', content[:1])[0] >> 3
        framesize_len = (5 + 4 * framesize_nbits + 7) // 8
        pos = framesize_len + 2 + 2
        while True:
            if pos < len(content):
                header16 = compat_struct_unpack('<H', content[pos:pos + 2])[0]
                pos += 2
                tag_code = header16 >> 6
                tag_len = header16 & 63
                if tag_len == 63:
                    tag_len = compat_struct_unpack('<I', content[pos:pos + 4])[0]
                    pos += 4
                assert pos + tag_len <= len(content), "Tag %d ends at %d+%d - that's longer than the file (%d)" % (
                 tag_code, pos, tag_len, len(content))
                yield (tag_code, content[pos:pos + tag_len])
                pos += tag_len
# okay decompiling testbed_py/swfinterp.py
