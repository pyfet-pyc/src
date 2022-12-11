
def _setup_standard_streams(self):
    """
    Modify `env.stdout` and `env.stdout_isatty` based on args, if needed.

    """

    self.args.output_file_specified = bool(self.args.output_file)
    if self.args.download:
        # FIXME: Come up with a cleaner solution.
        if not self.args.output_file and not self.env.stdout_isatty:
            # Use stdout as the download output file.
            self.args.output_file = self.env.stdout
        # With `--download`, we write everything that would normally go to
        # `stdout` to `stderr` instead. Let's replace the stream so that
        # we don't have to use many `if`s throughout the codebase.
        # The response body will be treated separately.
        self.env.stdout = self.env.stderr
        self.env.stdout_isatty = self.env.stderr_isatty

    elif self.args.output_file:
        # When not `--download`ing, then `--output` simply replaces
        # `stdout`. The file is opened for appending, which isn't what
        # we want in this case.
        self.args.output_file.seek(0)
        try:
            self.args.output_file.truncate()
        except OSError as e:
            if e.errno == errno.EINVAL:
                # E.g. /dev/null on Linux.
                pass
            else:
                raise
        self.env.stdout = self.args.output_file
        self.env.stdout_isatty = False

    if self.args.quiet:
        self.env.quiet = self.args.quiet
        self.env.stderr = self.env.devnull
        if not (self.args.output_file_specified and not self.args.download):
            self.env.stdout = self.env.devnull
        self.env.apply_warnings_filter()
