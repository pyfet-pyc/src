
if __name__ == "__main__":

    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Pretty print json")
    parser.add_argument(
        "path",
        metavar="PATH",
        help="path to file, or - for stdin",
    )
    parser.add_argument(
        "-i",
        "--indent",
        metavar="SPACES",
        type=int,
        help="Number of spaces in an indent",
        default=2,
    )
    args = parser.parse_args()

    from pipenv.patched.pip._vendor.rich.console import Console

    console = Console()
    error_console = Console(stderr=True)

    try:
        if args.path == "-":
            json_data = sys.stdin.read()
        else:
            with open(args.path, "rt") as json_file:
                json_data = json_file.read()
    except Exception as error:
        error_console.print(f"Unable to read {args.path!r}; {error}")
        sys.exit(-1)
