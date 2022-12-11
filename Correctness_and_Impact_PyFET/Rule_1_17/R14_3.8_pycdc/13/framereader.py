def GOPFrameIterator(gop_reader, pix_fmt):
  dec = VideoStreamDecompressor(gop_reader.fn, gop_reader.vid_fmt, gop_reader.w, gop_reader.h, pix_fmt)
  yield from dec.read()