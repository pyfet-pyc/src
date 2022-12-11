def test_rich_print():
    console = rich.get_console()
    output = io.StringIO()
    backup_file = console.file
    try:
        console.file = output
        rich.print("foo", "bar")
        rich.print("foo\n")
        rich.print("foo\n\n")

    finally:
        console.file = backup_file