# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:44:18
# Size of source mod 2**32: 405 bytes


def tar_path(path, target_path, is_dir: bool):
    f = tempfile.NamedTemporaryFile()
    with tarfile.open(mode='w', fileobj=f) as (t):
        abs_path = os.path.abspath(path)
        arcname = os.path.basename(path) if is_dir else os.path.basename(target_path) or os.path.basename(path)
        t.add(abs_path, arcname=arcname)
    f.seek(0)
    return f
# okay decompiling testbed_py/test.py
