def parse_cmdline(*args, **query):
    """
    Parses command line arguments and returns
    query and request_options
    """

    if not args:
        show_usage()
        sys.exit(0)

    query_string = " ".join(args)
    parsed = urlparse.urlparse("https://srv:0/%s" % query_string)
    request_options = options.parse_args(
        urlparse.parse_qs(parsed.query, keep_blank_values=True))

    result = parsed.path.lstrip("/")
    if not query:
        result = ":firstpage"

    return result(request_options, *args, **query)
