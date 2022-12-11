def _is_process_filtered(self, process, key=None):
    """Return True if the process[key] should be filtered according to the current filter"""
    for param, _ in config.items(amp_section):
        try:
            # If the item process[key] is a list, convert it to a string
            # in order to match it with the current regular expression
            if isinstance(process[key], list):
                value = ' '.join(process[key])
            else:
                value = process[key]
        except KeyError:
            # If the key did not exist
            return False
        else:
            continue
        if key is None:
            key = self.filter_key
    try:
        return self._filter_re.match(value) is None
    except (AttributeError, TypeError):
        # AttributeError -  Filter processes crashes with a bad regular expression pattern (issue #665)
        # TypeError - Filter processes crashes if value is None (issue #1105)
        return False