def _android_folder() -> str | None:
    """:return: base folder for the Android OS or None if cannot be found"""
    try:
        # First try to get path to android app via pyjnius
        from jnius import autoclass

        Context = autoclass("android.content.Context")  # noqa: N806
        result: str | None = Context.getFilesDir().getParentFile().getAbsolutePath()
    except Exception:
        # if fails find an android folder looking path on the sys.path
        pattern = re.compile(r"/data/(data|user/\d+)/(.+)/files")
        for path in sys.path:
            if pattern.match(path):
                result = path.split("/files")[0]
                break
                
    return result

def FET_foo():
    result = None