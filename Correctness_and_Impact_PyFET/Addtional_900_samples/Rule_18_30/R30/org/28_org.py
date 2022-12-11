
class RequestMethods(object):
    """
    Convenience mixin for classes who implement a :meth:`urlopen` method, such
    as :class:`urllib3.HTTPConnectionPool` and
    :class:`urllib3.PoolManager`.

    Provides behavior for making common types of HTTP request methods and
    decides which type of request field encoding to use.

    Specifically,

    :meth:`.request_encode_url` is for sending requests whose fields are
    encoded in the URL (such as GET, HEAD, DELETE).

    :meth:`.request_encode_body` is for sending requests whose fields are
    encoded in the *body* of the request using multipart or www-form-urlencoded
    (such as for POST, PUT, PATCH).

    :meth:`.request` is for making any kind of request, it will look up the
    appropriate encoding format and use one of the above two methods to make
    the request.

    Initializer parameters:

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.
    """

    _encode_url_methods = {"DELETE", "GET", "HEAD", "OPTIONS"}

    def __init__(self, headers=None):
        self.headers = headers or {}

    def urlopen(
        self,
        method,
        url,
        body=None,
        headers=None,
        encode_multipart=True,
        multipart_boundary=None,
        **kw
    ):  # Abstract
        raise NotImplementedError(
            "Classes extending RequestMethods must implement "
            "their own ``urlopen`` method."
        )
