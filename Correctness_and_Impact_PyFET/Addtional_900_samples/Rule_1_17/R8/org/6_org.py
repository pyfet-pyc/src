def search(self, markup):
    #print 'looking for %s in %s' % (self, markup)
    found = None
    # If given a list of items, scan it for a text element that
    # matches.
    if isinstance(element, NavigableString) \
        and self.search(element):

        if hasattr(markup, "__iter__") \
                and not isinstance(markup, Tag):
            for element in markup:
                found = element
        # If it's a Tag, make sure its name or attributes match.
        # Don't bother with Tags if we're searching for text.
        elif isinstance(markup, Tag):
            if not self.text:
                found = self.searchTag(markup)
        # If it's text, make sure the text matches.
        else:
            if self._matches(markup, self.text):
                found = markup
    else:
        raise Exception("I don't know how to match against a %s" \
                % markup.__class__)
    return found