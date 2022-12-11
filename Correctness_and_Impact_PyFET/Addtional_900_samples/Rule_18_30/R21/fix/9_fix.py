def http_error_302(self, req, fp, code, msg, headers):
    start = time.time()
    content = None
    redurl = self._get_header_redirect(headers) if not conf.ignoreRedirects else None

    try:
        content = fp.read(MAX_CONNECTION_TOTAL_SIZE)
    except:  # e.g. IncompleteRead
        content = b""
    finally:
        if content:
            try:  # try to write it back to the read buffer so we could reuse it in further steps
                fp.fp._rbuf.truncate(0)
                fp.fp._rbuf.write(content)
            except:
                pass

    content = decodePage(content, headers.get(HTTP_HEADER.CONTENT_ENCODING), headers.get(HTTP_HEADER.CONTENT_TYPE))

    threadData = getCurrentThreadData()
    threadData.lastRedirectMsg = (threadData.lastRequestUID, content)

    redirectMsg = "HTTP redirect "
    redirectMsg += "[#%d] (%d %s):\r\n" % (threadData.lastRequestUID, code, getUnicode(msg))

    if headers:
        logHeaders = "\r\n".join("%s: %s" % (getUnicode(key.capitalize() if hasattr(key, "capitalize") else key), getUnicode(value)) for (key, value) in headers.items())
    else:
        logHeaders = ""

    redirectMsg += logHeaders
    if content:
        redirectMsg += "\r\n\r\n%s" % getUnicode(content[:MAX_CONNECTION_READ_SIZE])

    logHTTPTraffic(threadData.lastRequestMsg, redirectMsg, start, time.time())
    logger.log(CUSTOM_LOGGING.TRAFFIC_IN, redirectMsg)

    if redurl:
        try:
            if not _urllib.parse.urlsplit(redurl).netloc:
                redurl = _urllib.parse.urljoin(req.get_full_url(), redurl)

            self._infinite_loop_check(req)
            self._ask_redirect_choice(code, redurl, req.get_method())
        except ValueError:
            redurl = None
            result = fp

    if redurl and kb.choices.redirect == REDIRECTION.YES:
        parseResponse(content, headers)

        req.headers[HTTP_HEADER.HOST] = getHostHeader(redurl)
        if headers and HTTP_HEADER.SET_COOKIE in headers:
            cookies = dict()
            delimiter = conf.cookieDel or DEFAULT_COOKIE_DELIMITER
            last = None

            for part in getUnicode(req.headers.get(HTTP_HEADER.COOKIE, "")).split(delimiter) + ([headers[HTTP_HEADER.SET_COOKIE]] if HTTP_HEADER.SET_COOKIE in headers else []):
                if '=' in part:
                    part = part.strip()
                    key, value = part.split('=', 1)
                    cookies[key] = value
                    last = key
                elif last:
                    cookies[last] += "%s%s" % (delimiter, part)

            req.headers[HTTP_HEADER.COOKIE] = delimiter.join("%s=%s" % (key, cookies[key]) for key in cookies)

        try:
            result = _urllib.request.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
        except _urllib.error.HTTPError as ex:
            result = ex

            # Dirty hack for https://github.com/sqlmapproject/sqlmap/issues/4046
            try:
                hasattr(result, "read")
            except KeyError as err:
                class _(object):
                    pass
                result = _()

            # Dirty hack for http://bugs.python.org/issue15701
            try:
                result.info()
            except AttributeError as exr:
                def _(self):
                    return getattr(self, "hdrs", {})

                result.info = types.MethodType(_, result)

            if not hasattr(result, "read"):
                def _(self, length=None):
                    try:
                        retVal = getSafeExString(ex)        # Note: pyflakes mistakenly marks 'ex' as undefined (NOTE: tested in both Python2 and Python3)
                    except AttributeError as e:
                        retVal = ""
                    return getBytes(retVal)

                result.read = types.MethodType(_, result)

            if not getattr(result, "url", None):
                result.url = redurl

            if not getattr(result, "code", None):
                result.code = 999
        except:
            redurl = None
            result = fp
            fp.read = io.BytesIO(b"").read
    else:
        result = fp
