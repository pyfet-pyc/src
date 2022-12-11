# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 04:01:03
# Size of source mod 2**32: 887 bytes


def unzip(path: str, target_dir: str, overwrite: bool=True) -> Optional[Union[(str, Popen)]]:
    from localstack.utils.platform import is_debian
    use_native_cmd = is_debian() or is_command_available('unzip')
    if use_native_cmd:
        flags = ['-o'] if overwrite else []
        flags += ['-q']
        try:
            cmd = [
             'unzip'] + flags + [path]
        except Exception:
            error_str = truncate(max_length=200)
            LOG.info('Unable to use native "unzip" command (using fallback mechanism): %s', error_str)
# okay decompiling testbed_py/test.pyc
