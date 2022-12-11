def getPage(**kwargs):
    """
    This method connects to the target URL or proxy and returns
    the target URL page content
    """

    if conf.offline:
        return None, None, None

    url = kwargs.get("url", None) or conf.url
    get = kwargs.get("get", None)
    post = kwargs.get("post", None)
    method = kwargs.get("method", None)
    cookie = kwargs.get("cookie", None)
    ua = kwargs.get("ua", None) or conf.agent
    referer = kwargs.get("referer", None) or conf.referer
    host = kwargs.get("host", None) or conf.host
    direct_ = kwargs.get("direct", False)
    multipart = kwargs.get("multipart", None)
    silent = kwargs.get("silent", False)
    raise404 = kwargs.get("raise404", True)
    timeout = kwargs.get("timeout", None) or conf.timeout
    auxHeaders = kwargs.get("auxHeaders", None)
    response = kwargs.get("response", False)
    ignoreTimeout = kwargs.get("ignoreTimeout", False) or kb.ignoreTimeout or conf.ignoreTimeouts
    refreshing = kwargs.get("refreshing", False)
    retrying = kwargs.get("retrying", False)
    crawling = kwargs.get("crawling", False)
    checking = kwargs.get("checking", False)
    skipRead = kwargs.get("skipRead", False)
    finalCode = kwargs.get("finalCode", False)
    chunked = kwargs.get("chunked", False) or conf.chunked

    start = time.time()

    if isinstance(conf.delay, (int, float)) and conf.delay > 0:
        time.sleep(conf.delay)

    threadData = getCurrentThreadData()
    with kb.locks.request:
        kb.requestCounter += 1
        threadData.lastRequestUID = kb.requestCounter

        if conf.proxyFreq:
            if kb.requestCounter % conf.proxyFreq == 1:
                conf.proxy = None

                warnMsg = "changing proxy"
                logger.warning(warnMsg)

                setHTTPHandlers()

    if conf.dummy or conf.murphyRate and randomInt() % conf.murphyRate == 0:
        if conf.murphyRate:
            time.sleep(randomInt() % (MAX_MURPHY_SLEEP_TIME + 1))

        page, headers, code = randomStr(int(randomInt()), alphabet=[_unichr(_) for _ in xrange(256)]), None, None if not conf.murphyRate else randomInt(3)

        threadData.lastPage = page
        threadData.lastCode = code

        return page, headers, code

    if conf.liveCookies:
        with kb.locks.liveCookies:
            if not checkFile(conf.liveCookies, raiseOnError=False) or os.path.getsize(conf.liveCookies) == 0:
                warnMsg = "[%s] [WARNING] live cookies file '%s' is empty or non-existent. Waiting for timeout (%d seconds)" % (time.strftime("%X"), conf.liveCookies, LIVE_COOKIES_TIMEOUT)
                dataToStdout(warnMsg)

                valid = False
                for _ in xrange(LIVE_COOKIES_TIMEOUT):
                    if checkFile(conf.liveCookies, raiseOnError=False) and os.path.getsize(conf.liveCookies) > 0:
                        valid = True
                        break
                    else:
                        dataToStdout('.')
                        time.sleep(1)

                dataToStdout("\n")

                if not valid:
                    errMsg = "problem occurred while loading cookies from file '%s'" % conf.liveCookies
                    raise SqlmapValueException(errMsg)

            cookie = openFile(conf.liveCookies).read().strip()
            cookie = re.sub(r"(?i)\ACookie:\s*", "", cookie)

    if multipart:
        post = multipart
    else:
        if not post:
            chunked = False

        elif chunked:
            post = _urllib.parse.unquote(post)
            post = chunkSplitPostData(post)

    webSocket = url.lower().startswith("ws")

    if not _urllib.parse.urlsplit(url).netloc:
        url = _urllib.parse.urljoin(conf.url, url)

    # flag to know if we are dealing with the same target host
    target = checkSameHost(url, conf.url)

    if not retrying:
        # Reset the number of connection retries
        threadData.retriesCount = 0

    # fix for known issue when urllib2 just skips the other part of provided
    # url splitted with space char while urlencoding it in the later phase
    url = url.replace(" ", "%20")

    if "://" not in url:
        url = "http://%s" % url

    conn = None
    page = None
    code = None
    status = None

    _ = _urllib.parse.urlsplit(url)
    requestMsg = u"HTTP request [#%d]:\r\n%s " % (threadData.lastRequestUID, method or (HTTPMETHOD.POST if post is not None else HTTPMETHOD.GET))
    requestMsg += getUnicode(("%s%s" % (_.path or "/", ("?%s" % _.query) if _.query else "")) if not any((refreshing, crawling, checking)) else url)
    responseMsg = u"HTTP response "
    requestHeaders = u""
    responseHeaders = None
    logHeaders = u""
    skipLogTraffic = False

    raise404 = raise404 and not kb.ignoreNotFound

    # support for non-latin (e.g. cyrillic) URLs as urllib/urllib2 doesn't
    # support those by default
    url = asciifyUrl(url)

    try:
        socket.setdefaulttimeout(timeout)

        if direct_:
            if '?' in url:
                url, params = url.split('?', 1)
                params = urlencode(params)
                url = "%s?%s" % (url, params)

        elif any((refreshing, crawling, checking)):
            pass

        elif target:
            if conf.forceSSL:
                url = re.sub(r"(?i)\A(http|ws):", r"\g<1>s:", url)
                url = re.sub(r"(?i):80/", ":443/", url)

            if PLACE.GET in conf.parameters and not get:
                get = conf.parameters[PLACE.GET]

                if not conf.skipUrlEncode:
                    get = urlencode(get, limit=True)

            if get:
                if '?' in url:
                    url = "%s%s%s" % (url, DEFAULT_GET_POST_DELIMITER, get)
                    requestMsg += "%s%s" % (DEFAULT_GET_POST_DELIMITER, get)
                else:
                    url = "%s?%s" % (url, get)
                    requestMsg += "?%s" % get

            if PLACE.POST in conf.parameters and not post and method != HTTPMETHOD.GET:
                post = conf.parameters[PLACE.POST]

        elif get:
            url = "%s?%s" % (url, get)
            requestMsg += "?%s" % get

        requestMsg += " %s" % _http_client.HTTPConnection._http_vsn_str

        # Prepare HTTP headers
        headers = forgeHeaders({HTTP_HEADER.COOKIE: cookie, HTTP_HEADER.USER_AGENT: ua, HTTP_HEADER.REFERER: referer, HTTP_HEADER.HOST: host}, base=None if target else {})

        if HTTP_HEADER.COOKIE in headers:
            cookie = headers[HTTP_HEADER.COOKIE]

        if kb.authHeader:
            headers[HTTP_HEADER.AUTHORIZATION] = kb.authHeader

        if kb.proxyAuthHeader:
            headers[HTTP_HEADER.PROXY_AUTHORIZATION] = kb.proxyAuthHeader

        if not conf.requestFile or not target:
            if not getHeader(headers, HTTP_HEADER.HOST):
                headers[HTTP_HEADER.HOST] = getHostHeader(url)

            if not getHeader(headers, HTTP_HEADER.ACCEPT):
                headers[HTTP_HEADER.ACCEPT] = HTTP_ACCEPT_HEADER_VALUE

            if not getHeader(headers, HTTP_HEADER.ACCEPT_ENCODING):
                headers[HTTP_HEADER.ACCEPT_ENCODING] = HTTP_ACCEPT_ENCODING_HEADER_VALUE if kb.pageCompress else "identity"

        elif conf.requestFile and getHeader(headers, HTTP_HEADER.USER_AGENT) == DEFAULT_USER_AGENT:
            for header in headers:
                if header.upper() == HTTP_HEADER.USER_AGENT.upper():
                    del headers[header]
                    break

        if post is not None and not multipart and not getHeader(headers, HTTP_HEADER.CONTENT_TYPE):
            headers[HTTP_HEADER.CONTENT_TYPE] = POST_HINT_CONTENT_TYPES.get(kb.postHint, DEFAULT_CONTENT_TYPE if unArrayizeValue(conf.base64Parameter) != HTTPMETHOD.POST else PLAIN_TEXT_CONTENT_TYPE)

        if headers.get(HTTP_HEADER.CONTENT_TYPE) == POST_HINT_CONTENT_TYPES[POST_HINT.MULTIPART]:
            warnMsg = "missing 'boundary parameter' in '%s' header. " % HTTP_HEADER.CONTENT_TYPE
            warnMsg += "Will try to reconstruct"
            singleTimeWarnMessage(warnMsg)

            boundary = findMultipartPostBoundary(conf.data)
            if boundary:
                headers[HTTP_HEADER.CONTENT_TYPE] = "%s; boundary=%s" % (headers[HTTP_HEADER.CONTENT_TYPE], boundary)

        if conf.keepAlive:
            headers[HTTP_HEADER.CONNECTION] = "keep-alive"

        if chunked:
            headers[HTTP_HEADER.TRANSFER_ENCODING] = "chunked"

        if auxHeaders:
            headers = forgeHeaders(auxHeaders, headers)

        if kb.headersFile:
            content = openFile(kb.headersFile, "rb").read()
            for line in content.split("\n"):
                line = getText(line.strip())
                if ':' in line:
                    header, value = line.split(':', 1)
                    headers[header] = value

        if conf.localhost:
            headers[HTTP_HEADER.HOST] = "localhost"

        for key, value in list(headers.items()):
            if key.upper() == HTTP_HEADER.ACCEPT_ENCODING.upper():
                value = re.sub(r"(?i)(,)br(,)?", lambda match: ',' if match.group(1) and match.group(2) else "", value) or "identity"

            del headers[key]
            if isinstance(value, six.string_types):
                for char in (r"\r", r"\n"):
                    value = re.sub(r"(%s)([^ \t])" % char, r"\g<1>\t\g<2>", value)
                headers[getBytes(key) if six.PY2 else key] = getBytes(value.strip("\r\n"))  # Note: Python3 has_header() expects non-bytes value

        if six.PY2:
            url = getBytes(url)  # Note: Python3 requires text while Python2 has problems when mixing text with binary POST

        if webSocket:
            ws = websocket.WebSocket()
            ws.settimeout(WEBSOCKET_INITIAL_TIMEOUT if kb.webSocketRecvCount is None else timeout)
            ws.connect(url, header=("%s: %s" % _ for _ in headers.items() if _[0] not in ("Host",)), cookie=cookie)  # WebSocket will add Host field of headers automatically
            ws.send(urldecode(post or ""))

            _page = []

            if kb.webSocketRecvCount is None:
                while True:
                    try:
                        _page.append(ws.recv())
                    except websocket.WebSocketTimeoutException:
                        kb.webSocketRecvCount = len(_page)
                        break
            else:
                for i in xrange(max(1, kb.webSocketRecvCount)):
                    _page.append(ws.recv())

            page = "\n".join(_page)

            ws.close()
            code = ws.status
            status = _http_client.responses[code]

            class _(dict):
                pass

            responseHeaders = _(ws.getheaders())
            responseHeaders.headers = ["%s: %s\r\n" % (_[0].capitalize(), _[1]) for _ in responseHeaders.items()]

            requestHeaders += "\r\n".join(["%s: %s" % (getUnicode(key.capitalize() if hasattr(key, "capitalize") else key), getUnicode(value)) for (key, value) in responseHeaders.items()])
            requestMsg += "\r\n%s" % requestHeaders

            if post is not None:
                requestMsg += "\r\n\r\n%s" % getUnicode(post)

            requestMsg += "\r\n"

            threadData.lastRequestMsg = requestMsg

            logger.log(CUSTOM_LOGGING.TRAFFIC_OUT, requestMsg)
        else:
            post = getBytes(post)

            if unArrayizeValue(conf.base64Parameter) == HTTPMETHOD.POST:
                if kb.place != HTTPMETHOD.POST:
                    conf.data = getattr(conf.data, UNENCODED_ORIGINAL_VALUE, conf.data)
                else:
                    post = urldecode(post, convall=True)
                    post = encodeBase64(post)

            if target and cmdLineOptions.method or method and method not in (HTTPMETHOD.GET, HTTPMETHOD.POST):
                req = MethodRequest(url, post, headers)
                req.set_method(cmdLineOptions.method or method)
            elif url is not None:
                req = _urllib.request.Request(url, post, headers)
            else:
                return None, None, None

            for function in kb.preprocessFunctions:
                try:
                    function(req)
                except Exception as ex:
                    errMsg = "error occurred while running preprocess "
                    errMsg += "function '%s' ('%s')" % (function.__name__, getSafeExString(ex))
                    raise SqlmapGenericException(errMsg)
                else:
                    post, headers = req.data, req.headers

            requestHeaders += "\r\n".join(["%s: %s" % (getUnicode(key.capitalize() if hasattr(key, "capitalize") else key), getUnicode(value)) for (key, value) in req.header_items()])

            if not getRequestHeader(req, HTTP_HEADER.COOKIE) and conf.cj:
                conf.cj._policy._now = conf.cj._now = int(time.time())
                cookies = conf.cj._cookies_for_request(req)
                requestHeaders += "\r\n%s" % ("Cookie: %s" % ";".join("%s=%s" % (getUnicode(cookie.name), getUnicode(cookie.value)) for cookie in cookies))

            if post is not None:
                if not getRequestHeader(req, HTTP_HEADER.CONTENT_LENGTH) and not chunked:
                    requestHeaders += "\r\n%s: %d" % (string.capwords(HTTP_HEADER.CONTENT_LENGTH), len(post))

            if not getRequestHeader(req, HTTP_HEADER.CONNECTION):
                requestHeaders += "\r\n%s: %s" % (HTTP_HEADER.CONNECTION, "close" if not conf.keepAlive else "keep-alive")

            requestMsg += "\r\n%s" % requestHeaders

            if post is not None:
                requestMsg += "\r\n\r\n%s" % getUnicode(post)

            if not chunked:
                requestMsg += "\r\n"

            if not multipart:
                threadData.lastRequestMsg = requestMsg

                logger.log(CUSTOM_LOGGING.TRAFFIC_OUT, requestMsg)

            if conf.cj:
                for cookie in conf.cj:
                    if cookie.value is None:
                        cookie.value = ""
                    else:
                        for char in (r"\r", r"\n"):
                            cookie.value = re.sub(r"(%s)([^ \t])" % char, r"\g<1>\t\g<2>", cookie.value)

            conn = _urllib.request.urlopen(req)

            if not kb.authHeader and getRequestHeader(req, HTTP_HEADER.AUTHORIZATION) and (conf.authType or "").lower() == AUTH_TYPE.BASIC.lower():
                kb.authHeader = getUnicode(getRequestHeader(req, HTTP_HEADER.AUTHORIZATION))

            if not kb.proxyAuthHeader and getRequestHeader(req, HTTP_HEADER.PROXY_AUTHORIZATION):
                kb.proxyAuthHeader = getRequestHeader(req, HTTP_HEADER.PROXY_AUTHORIZATION)

            # Return response object
            if response:
                return conn, None, None

            # Get HTTP response
            if hasattr(conn, "redurl"):
                page = (threadData.lastRedirectMsg[1] if kb.choices.redirect == REDIRECTION.NO else Connect._connReadProxy(conn)) if not skipRead else None
                skipLogTraffic = kb.choices.redirect == REDIRECTION.NO
                code = conn.redcode if not finalCode else code
            else:
                page = Connect._connReadProxy(conn) if not skipRead else None

            if conn:
                code = (code or conn.code) if conn.code == kb.originalCode else conn.code  # do not override redirection code (for comparison purposes)
                responseHeaders = conn.info()
                responseHeaders[URI_HTTP_HEADER] = conn.geturl() if hasattr(conn, "geturl") else url

                if hasattr(conn, "redurl"):
                    responseHeaders[HTTP_HEADER.LOCATION] = conn.redurl

                responseHeaders = patchHeaders(responseHeaders)
                kb.serverHeader = responseHeaders.get(HTTP_HEADER.SERVER, kb.serverHeader)
            else:
                code = None
                responseHeaders = {}

            page = decodePage(page, responseHeaders.get(HTTP_HEADER.CONTENT_ENCODING), responseHeaders.get(HTTP_HEADER.CONTENT_TYPE), percentDecode=not crawling)
            status = getUnicode(conn.msg) if conn and getattr(conn, "msg", None) else None

        kb.connErrorCounter = 0

        if not refreshing:
            refresh = responseHeaders.get(HTTP_HEADER.REFRESH, "").split("url=")[-1].strip()

            if extractRegexResult(META_REFRESH_REGEX, page):
                refresh = extractRegexResult(META_REFRESH_REGEX, page)

                debugMsg = "got HTML meta refresh header"
                logger.debug(debugMsg)

            if not refresh:
                refresh = extractRegexResult(JAVASCRIPT_HREF_REGEX, page)

                if refresh:
                    debugMsg = "got Javascript redirect logic"
                    logger.debug(debugMsg)

            if refresh:
                if kb.alwaysRefresh is None:
                    msg = "got a refresh intent "
                    msg += "(redirect like response common to login pages) to '%s'. " % refresh
                    msg += "Do you want to apply it from now on? [Y/n]"

                    kb.alwaysRefresh = readInput(msg, default='Y', boolean=True)

                if kb.alwaysRefresh:
                    if re.search(r"\Ahttps?://", refresh, re.I):
                        url = refresh
                    else:
                        url = _urllib.parse.urljoin(url, refresh)

                    threadData.lastRedirectMsg = (threadData.lastRequestUID, page)
                    kwargs["refreshing"] = True
                    kwargs["url"] = url
                    kwargs["get"] = None
                    kwargs["post"] = None

                    try:
                        return Connect._getPageProxy(**kwargs)
                    except SqlmapSyntaxException:
                        pass

        # Explicit closing of connection object
        if conn and not conf.keepAlive:
            try:
                if hasattr(conn.fp, '_sock'):
                    conn.fp._sock.close()
                conn.close()
            except Exception as ex:
                warnMsg = "problem occurred during connection closing ('%s')" % getSafeExString(ex)
                logger.warning(warnMsg)

    except SqlmapConnectionException as ex:
        if conf.proxyList and not kb.threadException:
            warnMsg = "unable to connect to the target URL ('%s')" % getSafeExString(ex)
            logger.critical(warnMsg)
            threadData.retriesCount = conf.retries
            return Connect._retryProxy(**kwargs)
        else:
            raise

    except _urllib.error.HTTPError as ex:
        page = None
        responseHeaders = None

        if checking:
            return None, None, None

        try:
            page = ex.read() if not skipRead else None
            responseHeaders = ex.info()
            responseHeaders[URI_HTTP_HEADER] = ex.geturl()
            responseHeaders = patchHeaders(responseHeaders)
            page = decodePage(page, responseHeaders.get(HTTP_HEADER.CONTENT_ENCODING), responseHeaders.get(HTTP_HEADER.CONTENT_TYPE), percentDecode=not crawling)
        except socket.timeout as e:
            warnMsg = "connection timed out while trying "
            warnMsg += "to get error page information (%d)" % ex.code
            logger.warning(warnMsg)
            return None, None, None
        except KeyboardInterrupt:
            raise
        except:
            pass
        finally:
            page = getUnicode(page)
