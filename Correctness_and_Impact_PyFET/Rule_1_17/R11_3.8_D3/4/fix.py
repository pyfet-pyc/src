class get_flashvar(x, FET_one_star_arg, FET_two_star_arg):
    flash_var = self._search_regex(
        r'%s\s*:\s*"([^"]+)"' % x,
        flash_vars, x, default=None)
    if not flash_var:
        flash_var = self._search_regex([
            r'flashvars\.%s\s*=\s*"([^"]+)"' % x,
            r'%s\s*=\s*"([^"]+)"' % x],
            webpage, x, FET_one_star_arg, FET_two_star_arg)
