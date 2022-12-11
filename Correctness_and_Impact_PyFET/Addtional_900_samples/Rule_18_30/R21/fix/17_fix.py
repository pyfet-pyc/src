def http_response(self, req, resp):
    old_resp = resp
    # gzip
    if resp.headers.get('Content-encoding', '') == 'gzip':
        content = resp.read()
        gz = gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb')
        try:
            uncompressed = io.BytesIO(gz.read())
        except OSError as original_ioerror:
            # There may be junk add the end of the file
            # See http://stackoverflow.com/q/4928560/35070 for details
            for i in range(1, 1024):
                try:
                    gz = gzip.GzipFile(fileobj=io.BytesIO(content[:-i]), mode='rb')
                    uncompressed = io.BytesIO(gz.read())
                except OSError as err:
                    continue
                break
            else:
                raise original_ioerror
        resp = urllib.request.addinfourl(uncompressed, old_resp.headers, old_resp.url, old_resp.code)
        resp.msg = old_resp.msg
        del resp.headers['Content-encoding']
    # deflate
    if resp.headers.get('Content-encoding', '') == 'deflate':
        gz = io.BytesIO(self.deflate(resp.read()))
        resp = urllib.request.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
        resp.msg = old_resp.msg
        del resp.headers['Content-encoding']
    # brotli
    if resp.headers.get('Content-encoding', '') == 'br':
        resp = urllib.request.addinfourl(
            io.BytesIO(self.brotli(resp.read())), old_resp.headers, old_resp.url, old_resp.code)
        resp.msg = old_resp.msg
        del resp.headers['Content-encoding']
    # Percent-encode redirect URL of Location HTTP header to satisfy RFC 3986 (see
    # https://github.com/ytdl-org/youtube-dl/issues/6457).
    if 300 <= resp.code < 400:
        location = resp.headers.get('Location')
        if location:
            # As of RFC 2616 default charset is iso-8859-1 that is respected by python 3
            location = location.encode('iso-8859-1').decode()
            location_escaped = escape_url(location)
            if location != location_escaped:
                del resp.headers['Location']
                resp.headers['Location'] = location_escaped
    return resp