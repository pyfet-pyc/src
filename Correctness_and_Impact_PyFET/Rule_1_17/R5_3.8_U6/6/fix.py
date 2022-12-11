def get_module_and_inject_docstring(file_path):
    """Replaces the docstring of the module with the changed file's content.

    Args:
      file_path: Path to the file

    Returns:
      A list containing the module changed by the file.
    """

    file_path = os.path.abspath(file_path)
    mod_index = file_path.find(PACKAGE.replace(".", os.sep))
    file_mod_name, _ = os.path.splitext(file_path[mod_index:])
    file_module = sys.modules[file_mod_name.replace(os.sep, ".")]

    # with open(file_path, "r") as f:
    f = open(file_path, "r")
    return f.read()