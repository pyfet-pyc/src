def check_against_path(self, path: str) -> None:
    with open(path, "rb") as file:
        return self.check_against_file(file)