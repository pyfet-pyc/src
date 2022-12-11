def _parse_options(options):
    """Parse search options string into optiond_dict
    """

    if options is None:
        return {}

    search_options = {
        'insensitive',
        'word_boundaries',
        'recursive',
    }
    return search_options