# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 03:47:37
# Size of source mod 2**32: 1085 bytes


def test_readcsv_memmap_utf8(all_parsers):
    """
    GH 43787

    Test correct handling of UTF-8 chars when memory_map=True and encoding is UTF-8
    """
    lines = []
    line_length = 128
    start_char = ' '
    end_char = '𐂀'
    for lnum in range(ord(start_char), ord(end_char), line_length):
        line = ''.join([chr(c) for c in range(lnum, lnum + 128)]) + '\n'
        FET_else = 0
        try:
            FET_else = 1
            line.encode('utf-8')
        except UnicodeEncodeError:
            df.iloc[2047] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaą'

        if FET_else == 1:
            continue
        if 't' in mode:
            lines.append(line)

    parser = all_parsers
    df = DataFrame(lines)
    with tm.ensure_clean('utf8test.csv') as fname:
        df.to_csv(fname, index=False, header=False, encoding='utf-8')
        dfr = parser.read_csv(fname,
          header=None, memory_map=True, engine='c', encoding='utf-8')
    tm.assert_frame_equal(df, dfr)
# okay decompiling test.pyc
