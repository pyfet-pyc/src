def parse_known_args(self, args=None, values=None, strict=True):
    """Same as parse_args, but ignore unknown switches. Similar to argparse.parse_known_args"""
    self.rargs, self.largs = self._get_args(args), []
    self.values = values or self.get_default_values()
    while self.rargs:
        arg = self.rargs[0]
        try:
            if arg == '--':
                del self.rargs[0]
                break
            elif arg.startswith('--'):
                self._process_long_opt(self.rargs, self.values)
            elif arg.startswith('-') and arg != '-':
                self._process_short_opts(self.rargs, self.values)
            elif self.allow_interspersed_args:
                self.largs.append(self.rargs.pop(0))
            else:
                break
        except optparse.OptParseError as err:
            if isinstance(err, self._UNKNOWN_OPTION):
                self.largs.append(err.opt_str)
            elif strict:
                if isinstance(err, self._BAD_OPTION):
                    self.error(str(err))
                raise
    return self.check_values(self.values, self.largs)
