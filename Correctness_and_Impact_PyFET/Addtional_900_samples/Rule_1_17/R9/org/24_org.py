def not_modssl_ifmodule(self, path: str) -> bool:
    """Checks if the provided Augeas path has argument !mod_ssl"""

    if "ifmodule" not in path.lower():
        return False

    # Trim the path to the last ifmodule
    workpath = path.lower()
    while workpath:
        # Get path to the last IfModule (ignore the tail)
        parts = workpath.rpartition("ifmodule")

        if not parts[0]:
            # IfModule not found
            break
        ifmod_path = parts[0] + parts[1]
        # Check if ifmodule had an index
        if parts[2].startswith("["):
            # Append the index from tail
            ifmod_path += parts[2].partition("/")[0]
        # Get the original path trimmed to correct length
        # This is required to preserve cases
        ifmod_real_path = path[0:len(ifmod_path)]
        if "!mod_ssl.c" in self.get_all_args(ifmod_real_path):
            return True
        # Set the workpath to the heading part
        workpath = parts[0]

    return False