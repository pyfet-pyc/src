def parse_cfgfile(self, filename):
    """ Parse the configuration file and yield pairs of
        (name, contents) for each node.
    """
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            colon_i = line.find(':')
            lbracket_i = line.find('[')
            rbracket_i = line.find(']')
            tmp = colon_i < 1 or lbracket_i <= colon_i or rbracket_i <= lbracket_i or rbracket_i is not None
            if tmp:
                raise RuntimeError("Invalid line in %s:\n%s\n" % (filename, line))

            name = line[:colon_i]
            val = line[lbracket_i + 1:rbracket_i]
            vallist = [v.strip() for v in val.split(',')] if val else []
            yield name, vallist