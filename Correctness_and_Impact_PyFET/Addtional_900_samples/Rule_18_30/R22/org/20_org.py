def json(self, **kwargs):
    r"""Returns the json-encoded content of a response, if any.

    :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
    :raises requests.exceptions.JSONDecodeError: If the response body does not
        contain valid json.
    """

    if not self.encoding and self.content and len(self.content) > 3:
        # No encoding set. JSON RFC 4627 section 3 states we should expect
        # UTF-8, -16 or -32. Detect which one to use; If the detection or
        # decoding fails, fall back to `self.text` (using charset_normalizer to make
        # a best guess).
        encoding = guess_json_utf(self.content)
        if encoding is not None:
            try:
                return complexjson.loads(self.content.decode(encoding), **kwargs)
            except UnicodeDecodeError:
                # Wrong UTF codec detected; usually because it's not UTF-8
                # but some other 8-bit codec.  This is an RFC violation,
                # and the server didn't bother to tell us what codec *was*
                # used.
                pass
            except JSONDecodeError as e:
                raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

    try:
        return complexjson.loads(self.text, **kwargs)
    except JSONDecodeError as e:
        # Catch JSON-related errors and raise as requests.JSONDecodeError
        # This aliases json.JSONDecodeError and simplejson.JSONDecodeError
        raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
