# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/generic_proxy.py
# Compiled at: 2022-08-11 19:52:21
# Size of source mod 2**32: 1741 bytes


def append_cors_headers(request_headers: Dict=None, response: Union[(Response, LambdaResponse)]=None):
    if config.DISABLE_CORS_HEADERS:
        return
    headers = {} if response is None else response.headers
    if isinstance(response, LambdaResponse):
        for key in response.multi_value_headers.keys():
            headers_list = list(response.multi_value_headers[key]) + [response.headers.get(key)]
            headers_list = [str(h) for h in headers_list if h is not None]
            headers[key] = ','.join(headers_list)

    if ACL_ORIGIN not in headers:
        headers[ACL_ORIGIN] = request_headers['origin'] if request_headers.get('origin') and not config.DISABLE_CORS_CHECKS else '*'
    if ACL_METHODS not in headers:
        headers[ACL_METHODS] = ','.join(CORS_ALLOWED_METHODS)
    if ACL_ALLOW_HEADERS not in headers:
        requested_headers = headers.get(ACL_REQUEST_HEADERS, '')
        requested_headers = re.split('[,\\s]+', requested_headers) + CORS_ALLOWED_HEADERS
        headers[ACL_ALLOW_HEADERS] = ','.join([h for h in requested_headers if h])
    if ACL_EXPOSE_HEADERS not in headers:
        headers[ACL_EXPOSE_HEADERS] = ','.join(CORS_EXPOSE_HEADERS)
    for header in ALLOWED_CORS_RESPONSE_HEADERS:
        if headers.get(header) == '':
            del headers[header]
# okay decompiling testbed_py/generic_proxy.py
