# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:42:09
# Size of source mod 2**32: 569 bytes


def get_module_and_inject_docstring(file_path):
    """Replaces the docstring of the module with the changed file's content.

    Args:
      file_path: Path to the file

    Returns:
      A list containing the module changed by the file.
    """
    file_path = os.path.abspath(file_path)
    mod_index = file_path.find(PACKAGE.replace('.', os.sep))
    file_mod_name, _ = os.path.splitext(file_path[mod_index:])
    file_module = sys.modules[file_mod_name.replace(os.sep, '.')]
    f = open(file_path, 'r')
    return f.read()
# okay decompiling test.pyc
