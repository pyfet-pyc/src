def debug(self, fmt, *args, **kwargs):
    if self.min_level > DEBUG:
        return
    self.log('DEBUG', self.debug_color, '21610b', fmt, *args, **kwargs)
