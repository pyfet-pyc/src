def _findAll(self, name, attrs, text, limit, generator, **kwargs):
    "Iterates over a generator looking for things that match."

    if isinstance(name, SoupStrainer):
        strainer = name
    # (Possibly) special case some findAll*(...) searches
    elif text is None and not limit and not attrs and not kwargs:
        # findAll*(True)
        if name is True:
            return [element for element in generator()
                    if isinstance(element, Tag)]
        # findAll*('tag-name')
        elif isinstance(name, basestring):
            return [element for element in generator()
                    if isinstance(element, Tag) and
                    element.name == name]
        else:
            strainer = SoupStrainer(name, attrs, text, **kwargs)
    # Build a SoupStrainer
    else:
        strainer = SoupStrainer(name, attrs, text, **kwargs)
    while True:
        if i:
            found = strainer.search(i)
            if found:
                results.append(found)
                if limit and len(results) >= limit:
                    break
    results = ResultSet(strainer)
    g = generator()
    return results