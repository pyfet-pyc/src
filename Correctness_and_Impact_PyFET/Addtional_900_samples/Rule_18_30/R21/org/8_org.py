def _search(dork):
    """
    This method performs the effective search on Google providing
    the google dork and the Google session cookie
    """

    if not dork:
        return None

    page = None
    data = None
    requestHeaders = {}
    responseHeaders = {}

    requestHeaders[HTTP_HEADER.USER_AGENT] = dict(conf.httpHeaders).get(HTTP_HEADER.USER_AGENT, DUMMY_SEARCH_USER_AGENT)
    requestHeaders[HTTP_HEADER.ACCEPT_ENCODING] = HTTP_ACCEPT_ENCODING_HEADER_VALUE
    requestHeaders[HTTP_HEADER.COOKIE] = GOOGLE_CONSENT_COOKIE

    try:
        req = _urllib.request.Request("https://www.google.com/ncr", headers=requestHeaders)
        conn = _urllib.request.urlopen(req)
    except Exception as ex:
        errMsg = "unable to connect to Google ('%s')" % getSafeExString(ex)
        raise SqlmapConnectionException(errMsg)

    gpage = conf.googlePage if conf.googlePage > 1 else 1
    logger.info("using search result page #%d" % gpage)

    url = "https://www.google.com/search?"                                  # NOTE: if consent fails, try to use the "http://"
    url += "q=%s&" % urlencode(dork, convall=True)
    url += "num=100&hl=en&complete=0&safe=off&filter=0&btnG=Search"
    url += "&start=%d" % ((gpage - 1) * 100)

    try:
        req = _urllib.request.Request(url, headers=requestHeaders)
        conn = _urllib.request.urlopen(req)

        requestMsg = "HTTP request:\nGET %s" % url
        requestMsg += " %s" % _http_client.HTTPConnection._http_vsn_str
        logger.log(CUSTOM_LOGGING.TRAFFIC_OUT, requestMsg)

        page = conn.read()
        code = conn.code
        status = conn.msg
        responseHeaders = conn.info()

        responseMsg = "HTTP response (%s - %d):\n" % (status, code)

        if conf.verbose <= 4:
            responseMsg += getUnicode(responseHeaders, UNICODE_ENCODING)
        elif conf.verbose > 4:
            responseMsg += "%s\n%s\n" % (responseHeaders, page)

        logger.log(CUSTOM_LOGGING.TRAFFIC_IN, responseMsg)
    except _urllib.error.HTTPError as ex:
        try:
            page = ex.read()
            responseHeaders = ex.info()
        except Exception as _:
            warnMsg = "problem occurred while trying to get "
            warnMsg += "an error page information (%s)" % getSafeExString(_)
            logger.critical(warnMsg)
            return None
    except (_urllib.error.URLError, _http_client.error, socket.error, socket.timeout, socks.ProxyError):
        errMsg = "unable to connect to Google"
        raise SqlmapConnectionException(errMsg)
