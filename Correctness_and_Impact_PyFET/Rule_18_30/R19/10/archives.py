def unzip(path: str, target_dir: str, overwrite: bool = True) -> Optional[Union[str, Popen]]:
    from localstack.utils.platform import is_debian

    use_native_cmd = is_debian() or is_command_available("unzip")
    if use_native_cmd:
        # Running the native command can be an order of magnitude faster in the container. Also, `unzip`
        #  is capable of extracting zip files with incorrect CRC codes (sometimes happens, e.g., with some
        #  Node.js/Serverless versions), which can fail with Python's `zipfile` (extracting empty files).
        flags = ["-o"] if overwrite else []
        flags += ["-q"]
        try:
            cmd = ["unzip"] + flags + [path]
        except Exception:
            error_str = truncate(max_length=200)
            LOG.info(
                'Unable to use native "unzip" command (using fallback mechanism): %s', error_str
            )