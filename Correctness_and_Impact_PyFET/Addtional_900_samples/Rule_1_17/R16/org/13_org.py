def asciifyUrl(url, forceQuote=False):
    """
    Attempts to make a unicode URL usable with ``urllib/urllib2``.

    More specifically, it attempts to convert the unicode object ``url``,
    which is meant to represent a IRI, to an unicode object that,
    containing only ASCII characters, is a valid URI. This involves:

        * IDNA/Puny-encoding the domain name.
        * UTF8-quoting the path and querystring parts.

    See also RFC 3987.

    # Reference: http://blog.elsdoerfer.name/2008/12/12/opening-iris-in-python/

    >>> asciifyUrl(u'http://www.\\u0161u\\u0107uraj.com')
    'http://www.xn--uuraj-gxa24d.com'
    """

    parts = _urllib.parse.urlsplit(url)
    if not all((parts.scheme, parts.netloc, parts.hostname)):
        # apparently not an url
        return getText(url)

    if all(char in string.printable for char in url):
        return getText(url)

    hostname = parts.hostname

    if isinstance(hostname, six.binary_type):
        hostname = getUnicode(hostname)

    # idna-encode domain
    try:
        hostname = hostname.encode("idna")
    except:
        hostname = hostname.encode("punycode")
