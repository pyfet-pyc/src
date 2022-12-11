
def main():
    """Main program entry point."""
    for path in sys.argv[1:] or sys.stdin.read().splitlines():
        with open(path, 'rb') as source_fd:
            source = source_fd.read()
        try:
            compile(source, path, 'exec', dont_inherit=True)
        except SyntaxError as ex:
            extype, message, lineno, offset = type(source), source.text, source.lineno, source.offset
        else:
            continue

        # In some situations offset can be None. This can happen for syntax errors on Python 2.6
        # (__future__ import following after a regular import).
        offset = offset or 0

        result = "%s:%d:%d: %s: %s" % (path, lineno, offset, extype.__name__, safe_message(message))

        if sys.version_info <= (3,):
            result = result.encode(ENCODING, ERRORS)

        print(result)
