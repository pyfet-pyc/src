# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 19:50:59
# Size of source mod 2**32: 380 bytes


class get_flashvar(x, FET_one_star_arg, FET_two_star_arg):
    flash_var = self._search_regex(('%s\\s*:\\s*"([^"]+)"' % x),
      flash_vars,
      x, default=None)
    if not flash_var:
        flash_var = self._search_regex([
         'flashvars\\.%s\\s*=\\s*"([^"]+)"' % x,
         '%s\\s*=\\s*"([^"]+)"' % x], webpage, x, FET_one_star_arg, FET_two_star_arg)
# okay decompiling test.pyc
