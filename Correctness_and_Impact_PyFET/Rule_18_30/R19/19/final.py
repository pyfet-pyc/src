# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:53:01
# Size of source mod 2**32: 525 bytes


def _html_wrapper(data):
    """
    Convert ANSI text `data` to HTML
    """
    cmd = [
     'bash', CONFIG['path.internal.ansi2html'], '--palette=solarized', '--bg=dark']
    try:
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except FileNotFoundError:
        print('ERROR: %s' % cmd)
        raise
    else:
        data = data.encode('utf-8')
        stdout, stderr = proc.communicate(data)
        if proc.returncode != 0:
            error((stdout + stderr).decode('utf-8'))
        return stdout.decode('utf-8')
# okay decompiling testbed_py/test.pyc
