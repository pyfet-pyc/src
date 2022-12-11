def finish_starttag(self, tag, attrs):
    try:
        method = getattr(self, 'start_' + tag)
    except AttributeError as e:
        try:
            method = getattr(self, 'do_' + tag)
        except AttributeError as e:
            self.unknown_starttag(tag, attrs)
            return -1
        else:
            self.handle_starttag(tag, method, attrs)
            return 0
    else:
        self.stack.append(tag)
        self.handle_starttag(tag, method, attrs)
        return 1
