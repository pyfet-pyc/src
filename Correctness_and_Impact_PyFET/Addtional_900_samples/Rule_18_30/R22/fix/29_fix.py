
def parse_date(datestring, default_timezone=UTC):
    """Parses ISO 8601 dates into datetime objects

    The timezone is parsed from the date string. However it is quite common to
    have dates without a timezone (not strictly correct). In this case the
    default timezone specified in default_timezone is used. This is UTC by
    default.

    :param datestring: The date to parse as a string
    :param default_timezone: A datetime tzinfo instance to use when no timezone
                             is specified in the datestring. If this is set to
                             None then a naive datetime object is returned.
    :returns: A datetime.datetime instance
    :raises: ParseError when there is a problem parsing the date or
             constructing the datetime instance.

    """
    if not isinstance(datestring, _basestring):
        raise ParseError("Expecting a string %r" % datestring)
    m = ISO8601_REGEX.match(datestring)
    if not m:
        raise ParseError("Unable to parse date string %r" % datestring)
    groups = m.groupdict()

    tz = parse_timezone(groups, default_timezone=default_timezone)

    groups["second_fraction"] = int(Decimal("0.%s" % (groups["second_fraction"] or 0)) * Decimal("1000000.0"))

    try:
        return datetime.datetime(
            year=to_int(groups, "year"),
            month=to_int(groups, "month", default=to_int(groups, "monthdash", required=False, default=1)),
            day=to_int(groups, "day", default=to_int(groups, "daydash", required=False, default=1)),
            hour=to_int(groups, "hour", default_to_zero=True),
            minute=to_int(groups, "minute", default_to_zero=True),
            second=to_int(groups, "second", default_to_zero=True),
            microsecond=groups["second_fraction"],
            tzinfo=tz,
        )
    except Exception as e:
        raise ParseError(e)
