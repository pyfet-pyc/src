
def _parse_items(self):
    """
    Parse `args.request_items` into `args.headers`, `args.data`,
    `args.params`, and `args.files`.

    """
    try:
        request_items = RequestItems.from_args(
            request_item_args=self.args.request_items,
            request_type=self.args.request_type,
        )
    except ParseError as e:
        if self.args.traceback:
            raise
        self.error(e.args[0])
    else:
        self.args.headers = request_items.headers
        self.args.data = request_items.data
        self.args.files = request_items.files
        self.args.params = request_items.params
        self.args.multipart_data = request_items.multipart_data

    if self.args.files and not self.args.form:
        # `http url @/path/to/file`
        request_file = None
        for key, file in self.args.files.items():
            if key != '':
                self.error(
                    'Invalid file fields (perhaps you meant --form?):'
                    f' {",".join(self.args.files.keys())}')
            if request_file is not None:
                self.error("Can't read request from multiple files")
            request_file = file

        fn, fd, ct = request_file
        self.args.files = {}

        self._body_from_file(fd)

        if 'Content-Type' not in self.args.headers:
            content_type = get_content_type(fn)
            if content_type:
                self.args.headers['Content-Type'] = content_type
