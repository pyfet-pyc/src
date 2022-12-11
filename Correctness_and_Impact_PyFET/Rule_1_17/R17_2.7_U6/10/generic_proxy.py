
def append_cors_headers(
    request_headers: Dict = None, response: Union[Response, LambdaResponse] = None
):
    # use this config to disable returning CORS headers entirely (more restrictive security setting)
    if config.DISABLE_CORS_HEADERS:
        return

    # Note: Use "response is None" here instead of "not response"
    headers = {} if response is None else response.headers

    # In case we have LambdaResponse, copy multivalue headers to regular headers, since
    # CaseInsensitiveDict does not support "__contains__" and it's easier to deal with
    # a single headers object
    if isinstance(response, LambdaResponse):
        for key in response.multi_value_headers.keys():
            headers_list = list(response.multi_value_headers[key]) + [response.headers.get(key)]
            headers_list = [str(h) for h in headers_list if h is not None]
            headers[key] = ",".join(headers_list)


    if ACL_ORIGIN not in headers:
        headers[ACL_ORIGIN] = (
            request_headers["origin"]
            if request_headers.get("origin") and not config.DISABLE_CORS_CHECKS
            else "*"
        )
    if ACL_METHODS not in headers:
        headers[ACL_METHODS] = ",".join(CORS_ALLOWED_METHODS)
    if ACL_ALLOW_HEADERS not in headers:
        requested_headers = headers.get(ACL_REQUEST_HEADERS, "")
        requested_headers = re.split(r"[,\s]+", requested_headers) + CORS_ALLOWED_HEADERS
        headers[ACL_ALLOW_HEADERS] = ",".join([h for h in requested_headers if h])
    if ACL_EXPOSE_HEADERS not in headers:
        headers[ACL_EXPOSE_HEADERS] = ",".join(CORS_EXPOSE_HEADERS)

    for header in ALLOWED_CORS_RESPONSE_HEADERS:
        if headers.get(header) == "":
            del headers[header]