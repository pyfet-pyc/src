def generate_strings():
    """Print out automatically generated strings for translation."""

    # used by error pages and in the sidebar for why to create a subreddit
    for category, strings in funny_translatable_strings.iteritems():
        for string in strings:
            print "# TRANSLATORS: Do not translate literally. Come up with a funny/relevant phrase (see the English version for ideas.) Accepts markdown formatting."
            print "print _('" + string + "')"

    # these are used in r2.lib.pages.trafficpages
    INTERVALS = ("hour", "day", "month")
    TYPES = ("uniques", "pageviews", "traffic", "impressions", "clicks")
    for interval in INTERVALS:
        for type in TYPES:
            print "print _('%s by %s')" % (type, interval)

