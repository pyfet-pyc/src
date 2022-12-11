def prepare_url(self, url, params):
    """Prepares the given HTTP URL."""
    #: Accept objects that have string representations.
    #: We're unable to blindly call unicode/str functions
    #: as this will include the bytestring indicator (b'')
    #: on python 3.x.
    #: https://github.com/psf/requests/pull/2238
    if isinstance(url, bytes):
        url = url.decode("utf8")
    else:
        url = str(url)

    # Remove leading whitespaces from url
    url = url.lstrip()

    # Don't do any URL preparation for non-HTTP schemes like `mailto`,
    # `data` etc to work around exceptions from `url_parse`, which
    # handles RFC 3986 only.
    if ":" in url and not url.lower().startswith("http"):
        self.url = url
        return

    # Support for unicode domain names and paths.
    try:
        scheme, auth, host, port, path, query, fragment = parse_url(url)
    except LocationParseError as e:
        raise InvalidURL(*e.args)

    if not scheme:
        raise MissingSchema(
            f"Invalid URL {url!r}: No scheme supplied. "
            f"Perhaps you meant http://{url}?"
        )

    if not host:
        raise InvalidURL(f"Invalid URL {url!r}: No host supplied")

    # In general, we want to try IDNA encoding the hostname if the string contains
    # non-ASCII characters. This allows users to automatically get the correct IDNA
    # behaviour. For strings containing only ASCII characters, we need to also verify
    # it doesn't start with a wildcard (*), before allowing the unencoded hostname.
    if not unicode_is_ascii(host):
        try:
            host = self._get_idna_encoded_host(host)
        except UnicodeError:
            raise InvalidURL("URL has an invalid label.")
    elif host.startswith(("*", ".")):
        raise InvalidURL("URL has an invalid label.")
