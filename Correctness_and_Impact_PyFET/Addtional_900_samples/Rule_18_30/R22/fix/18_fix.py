def get_metadata(self, name: str) -> str:
    try:
        return self._metadata[name].decode()
    except UnicodeDecodeError as e:
        # Augment the default error with the origin of the file.
        raise UnsupportedWheel(
            f"Error decoding metadata for {self._wheel_name}: {e} in {name} file"
        )
