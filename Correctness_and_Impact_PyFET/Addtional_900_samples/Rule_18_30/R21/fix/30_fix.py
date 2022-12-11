def retry_after(cls, response: requests.Response, default: int) -> datetime.datetime:
    """Compute next `poll` time based on response ``Retry-After`` header.

    Handles integers and various datestring formats per
    https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37

    :param requests.Response response: Response from `poll`.
    :param int default: Default value (in seconds), used when
        ``Retry-After`` header is not present or invalid.

    :returns: Time point when next `poll` should be performed.
    :rtype: `datetime.datetime`

    """
    retry_after = response.headers.get('Retry-After', str(default))
    try:
        seconds = int(retry_after)
    except ValueError as err:
        # The RFC 2822 parser handles all of RFC 2616's cases in modern
        # environments (primarily HTTP 1.1+ but also py27+)
        when = parsedate_tz(retry_after)
        if when is not None:
            try:
                tz_secs = datetime.timedelta(when[-1] if when[-1] is not None else 0)
                return datetime.datetime(*when[:7]) - tz_secs
            except (ValueError, OverflowError) as err:
                pass
        seconds = default

    return datetime.datetime.now() + datetime.timedelta(seconds=seconds)
