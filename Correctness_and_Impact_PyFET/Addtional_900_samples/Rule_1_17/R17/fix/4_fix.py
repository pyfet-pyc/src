def rgba_to(pix_in, target_fmt, w, h, pitch=None):
    if not isinstance(pix_in, (bytes, bytearray)):
        pix_in = bytearray(pix_in)
    assert w > 0 and h > 0, "Must specify w and h"
    assert len(pix_in) == w * h * 4, "Invalid rgba data {}".format(pix_in)
    assert target_fmt in ('rgba', 'bgra', 'argb', 'abgr', 'rgb', 'bgr')

    if target_fmt == 'rgba':
        return pix_in

    pixels = [pix_in[i:i + 4] for i in range(0, len(pix_in), 4)]
    if target_fmt == 'bgra':
        return b''.join([bytes(p[:3][::-1] + p[3:]) for p in pixels])
    elif target_fmt == 'abgr':
        return b''.join([bytes(p[3:] + p[:3][::-1]) for p in pixels])
    elif target_fmt == 'argb':
        return b''.join([bytes(p[3:] + p[:3]) for p in pixels])

    # rgb/bgr, default to 4 byte alignment
    if pitch is None:
        pitch = ((3 * w) + 3) & ~3
    # Assume pitch 0 == unaligned
    elif pitch == 0:
        pitch = 3 * w

    out = b''
    padding = b'\x00' * (pitch - w * 3)
    for row in [pix_in[i:i + w * 4] for i in range(0, len(pix_in), w * 4)]:
        pixelrow = [row[i:i + 4] for i in range(0, len(row), 4)]
        if target_fmt == 'rgb':
            out += b''.join([bytes(p[:3]) for p in pixelrow])
        elif target_fmt == 'bgr':
            out += b''.join([bytes(p[:3][::-1]) for p in pixelrow])
        out += padding
    return out