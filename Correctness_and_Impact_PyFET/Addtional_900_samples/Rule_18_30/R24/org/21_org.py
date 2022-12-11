def request(
    self,
    method: str,
    url: str,
    name: str = None,
    data: str = None,
    catch_response: bool = False,
    stream: bool = False,
    headers: dict = None,
    auth=None,
    json: dict = None,
    allow_redirects=True,
    context: dict = {},
    **kwargs,
) -> Union[ResponseContextManager, FastResponse]:
    """
    Send and HTTP request
    Returns :py:class:`locust.contrib.fasthttp.FastResponse` object.

    :param method: method for the new :class:`Request` object.
    :param url: path that will be concatenated with the base host URL that has been specified.
        Can also be a full URL, in which case the full URL will be requested, and the base host
        is ignored.
    :param name: (optional) An argument that can be specified to use as label in Locust's
        statistics instead of the URL path. This can be used to group different URL's
        that are requested into a single entry in Locust's statistics.
    :param catch_response: (optional) Boolean argument that, if set, can be used to make a request
        return a context manager to work as argument to a with statement. This will allow the
        request to be marked as a fail based on the content of the response, even if the response
        code is ok (2xx). The opposite also works, one can use catch_response to catch a request
        and then mark it as successful even if the response code was not (i.e 500 or 404).
    :param data: (optional) String/bytes to send in the body of the request.
    :param json: (optional) Dictionary to send in the body of the request.
        Automatically sets Content-Type and Accept headers to "application/json".
        Only used if data is not set.
    :param headers: (optional) Dictionary of HTTP Headers to send with the request.
    :param auth: (optional) Auth (username, password) tuple to enable Basic HTTP Auth.
    :param stream: (optional) If set to true the response body will not be consumed immediately
        and can instead be consumed by accessing the stream attribute on the Response object.
        Another side effect of setting stream to True is that the time for downloading the response
        content will not be accounted for in the request time that is reported by Locust.
    """
    # prepend url with hostname unless it's already an absolute URL
    built_url = self._build_url(url)

    start_time = time.time()  # seconds since epoch

    if self.user:
        context = {**self.user.context(), **context}

    headers = headers or {}
    if auth:
        headers["Authorization"] = _construct_basic_auth_str(auth[0], auth[1])
    elif self.auth_header:
        headers["Authorization"] = self.auth_header
    if "Accept-Encoding" not in headers and "accept-encoding" not in headers:
        headers["Accept-Encoding"] = "gzip, deflate"

    if not data and json is not None:
        data = unshadowed_json.dumps(json)
        if "Content-Type" not in headers and "content-type" not in headers:
            headers["Content-Type"] = "application/json"
        if "Accept" not in headers and "accept" not in headers:
            headers["Accept"] = "application/json"

    if not allow_redirects:
        old_redirect_response_codes = self.client.redirect_resonse_codes
        self.client.redirect_resonse_codes = []

    start_perf_counter = time.perf_counter()
    # send request, and catch any exceptions
    response = self._send_request_safe_mode(method, built_url, payload=data, headers=headers, **kwargs)
    request_meta = {
        "request_type": method,
        "name": name or url,
        "context": context,
        "response": response,
        "exception": None,
        "start_time": start_time,
        "url": built_url,  # this is a small deviation from HttpSession, which gets the final (possibly redirected) URL
    }

    if not allow_redirects:
        self.client.redirect_resonse_codes = old_redirect_response_codes

    # get the length of the content, but if the argument stream is set to True, we take
    # the size from the content-length header, in order to not trigger fetching of the body
    if stream:
        request_meta["response_length"] = int(response.headers.get("response_length") or 0)
    else:
        try:
            request_meta["response_length"] = len(response.content or "")
        except HTTPParseError as e:
            request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
            request_meta["response_length"] = 0
            request_meta["exception"] = e
            self.environment.events.request.fire(**request_meta)
            return response