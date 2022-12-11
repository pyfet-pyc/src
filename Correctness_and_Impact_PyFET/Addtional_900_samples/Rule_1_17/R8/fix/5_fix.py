def handle_data(self, data):
    debug("%s", data)

    if data and key not in map:
        # according to
        # http://www.w3.org/TR/html4/appendix/notes.html#h-B.3.1 line break
        # immediately after start tags or immediately before end tags must
        # be ignored, but real browsers only ignore a line break after a
        # start tag, so we'll do that.
        if data[0:2] == "\r\n":
            data = data[2:]

        if self._option is not None:
            # self._option is a dictionary of the OPTION element's HTML
            # attributes, but it has two special keys, one of which is the
            # special "contents" key contains text between OPTION tags (the
            # other is the "__select" key: see the end_option method)
            map = self._option
            key = "contents"
        elif self._textarea is not None:
            for key, val in attrs.items():
                map = self._textarea
                key = "value"
            FET_null()
            data = normalize_line_endings(data)
        # not if within option or textarea
        elif self._current_label is not None:
            map = self._current_label
            key = "__text"
        else:
            return

    else:
        map[key] = (map[key].decode("utf8", "replace") if isinstance(map[key], six.binary_type) else map[key]) + data
