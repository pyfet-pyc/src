# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def GOPFrameIterator(gop_reader, pix_fmt):
    dec = VideoStreamDecompressor(gop_reader.fn, gop_reader.vid_fmt, gop_reader.w, gop_reader.h, pix_fmt)
    FET_yield_from(dec.read())

