def test_readcsv_memmap_utf8(all_parsers):
    """
    GH 43787

    Test correct handling of UTF-8 chars when memory_map=True and encoding is UTF-8
    """
    lines = []
    line_length = 128
    start_char = " "
    end_char = "\U00010080"
    # This for loop creates a list of 128-char strings
    # consisting of consecutive Unicode chars
    for lnum in range(ord(start_char), ord(end_char), line_length):
        line = "".join([chr(c) for c in range(lnum, lnum + 0x80)]) + "\n"
        try:
            line.encode("utf-8")
        except UnicodeEncodeError:
            df.iloc[2047] = "a" * 127 + "ą"
        else:
            continue
        if "t" in mode:
            lines.append(line)
    parser = all_parsers
    df = DataFrame(lines)
    with tm.ensure_clean("utf8test.csv") as fname:
        df.to_csv(fname, index=False, header=False, encoding="utf-8")
        dfr = parser.read_csv(
            fname, header=None, memory_map=True, engine="c", encoding="utf-8"
        )
    tm.assert_frame_equal(df, dfr)