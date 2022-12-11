def edit(self, text: t.Optional[t.AnyStr]) -> t.Optional[t.AnyStr]:
    import tempfile

    if not text:
        data = b""
    elif isinstance(text, (bytes, bytearray)):
        data = text
    else:
        if text and not text.endswith("\n"):
            text += "\n"

        if WIN:
            data = text.replace("\n", "\r\n").encode("utf-8-sig")
        else:
            data = text.encode("utf-8")

    fd, name = tempfile.mkstemp(prefix="editor-", suffix=self.extension)
    f: t.BinaryIO

    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)

        # If the filesystem resolution is 1 second, like Mac OS
        # 10.12 Extended, or 2 seconds, like FAT32, and the editor
        # closes very fast, require_save can fail. Set the modified
        # time to be 2 seconds in the past to work around this.
        os.utime(name, (os.path.getatime(name), os.path.getmtime(name) - 2))
        # Depending on the resolution, the exact value might not be
        # recorded, so get the new recorded value.
        timestamp = os.path.getmtime(name)

        self.edit_file(name)

        if self.require_save and os.path.getmtime(name) == timestamp:
            return None

        with open(name, "rb") as f:
            rv = f.read()

        if isinstance(text, (bytes, bytearray)):
            return rv

        return rv.decode("utf-8-sig").replace("\r\n", "\n")  # type: ignore
    finally:
        os.unlink(name)

