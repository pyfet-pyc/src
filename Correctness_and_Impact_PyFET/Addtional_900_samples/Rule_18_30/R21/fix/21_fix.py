def establish_connection():
    ctx.chunk_size = (random.randint(int(chunk_size * 0.95), chunk_size)
                        if not is_test and chunk_size else chunk_size)
    if ctx.resume_len > 0:
        range_start = ctx.resume_len
        if req_start is not None:
            # offset the beginning of Range to be within request
            range_start += req_start
        if ctx.is_resume:
            self.report_resuming_byte(ctx.resume_len)
        ctx.open_mode = 'ab'
    elif req_start is not None:
        range_start = req_start
    elif ctx.chunk_size > 0:
        range_start = 0
    else:
        range_start = None
    ctx.is_resume = False

    if ctx.chunk_size:
        chunk_aware_end = range_start + ctx.chunk_size - 1
        # we're not allowed to download outside Range
        range_end = chunk_aware_end if req_end is None else min(chunk_aware_end, req_end)
    elif req_end is not None:
        # there's no need for chunked downloads, so download until the end of Range
        range_end = req_end
    else:
        range_end = None

    if try_call(lambda: range_start > range_end):
        ctx.resume_len = 0
        ctx.open_mode = 'wb'
        raise RetryDownload(Exception(f'Conflicting range. (start={range_start} > end={range_end})'))

    if try_call(lambda: range_end >= ctx.content_len):
        range_end = ctx.content_len - 1

    request = sanitized_Request(url, request_data, headers)
    has_range = range_start is not None
    if has_range:
        request.add_header('Range', f'bytes={int(range_start)}-{int_or_none(range_end) or ""}')
    # Establish connection
    try:
        ctx.data = self.ydl.urlopen(request)
        # When trying to resume, Content-Range HTTP header of response has to be checked
        # to match the value of requested Range HTTP header. This is due to a webservers
        # that don't support resuming and serve a whole file with no Content-Range
        # set in response despite of requested Range (see
        # https://github.com/ytdl-org/youtube-dl/issues/6057#issuecomment-126129799)
        if has_range:
            content_range = ctx.data.headers.get('Content-Range')
            content_range_start, content_range_end, content_len = parse_http_range(content_range)
            # Content-Range is present and matches requested Range, resume is possible
            if range_start == content_range_start and (
                    # Non-chunked download
                    not ctx.chunk_size
                    # Chunked download and requested piece or
                    # its part is promised to be served
                    or content_range_end == range_end
                    or content_len < range_end):
                ctx.content_len = content_len
                if content_len or req_end:
                    ctx.data_len = min(content_len or req_end, req_end or content_len) - (req_start or 0)
                return
            # Content-Range is either not present or invalid. Assuming remote webserver is
            # trying to send the whole file, resume is not possible, so wiping the local file
            # and performing entire redownload
            self.report_unable_to_resume()
            ctx.resume_len = 0
            ctx.open_mode = 'wb'
        ctx.data_len = ctx.content_len = int_or_none(ctx.data.info().get('Content-length', None))
    except urllib.error.HTTPError as err:
        if err.code == 416:
            # Unable to resume (requested range not satisfiable)
            try:
                # Open the connection again without the range header
                ctx.data = self.ydl.urlopen(
                    sanitized_Request(url, request_data, headers))
                content_length = ctx.data.info()['Content-Length']
            except urllib.error.HTTPError as err:
                if err.code < 500 or err.code >= 600:
                    raise
            else:
                # Examine the reported length
                if (content_length is not None
                        and (ctx.resume_len - 100 < int(content_length) < ctx.resume_len + 100)):
                    # The file had already been fully downloaded.
                    # Explanation to the above condition: in issue #175 it was revealed that
                    # YouTube sometimes adds or removes a few bytes from the end of the file,
                    # changing the file size slightly and causing problems for some users. So
                    # I decided to implement a suggested change and consider the file
                    # completely downloaded if the file size differs less than 100 bytes from
                    # the one in the hard drive.
                    self.report_file_already_downloaded(ctx.filename)
                    self.try_rename(ctx.tmpfilename, ctx.filename)
                    self._hook_progress({
                        'filename': ctx.filename,
                        'status': 'finished',
                        'downloaded_bytes': ctx.resume_len,
                        'total_bytes': ctx.resume_len,
                    }, info_dict)
                    raise SucceedDownload()
                else:
                    # The length does not match, we start the download over
                    self.report_unable_to_resume()
                    ctx.resume_len = 0
                    ctx.open_mode = 'wb'
                    return
        elif err.code < 500 or err.code >= 600:
            # Unexpected HTTP error
            raise
        raise RetryDownload(err)
    except urllib.error.URLError as err:
        if isinstance(err.reason, ssl.CertificateError):
            raise
        raise RetryDownload(err)
    # In urllib.request.AbstractHTTPHandler, the response is partially read on request.
    # Any errors that occur during this will not be wrapped by URLError
    except RESPONSE_READ_EXCEPTIONS as err:
        raise RetryDownload(err)
