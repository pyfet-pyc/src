# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 00:11:04
# Size of source mod 2**32: 917 bytes


def get_ld_headers(file):
    """
    Parse the header of the loader section of executable and archives
    This function calls /usr/bin/dump -H as a subprocess
    and returns a list of (ld_header, ld_header_info) tuples.
    """
    ldr_headers = []
    p = Popen(['/usr/bin/dump', f"-X{AIX_ABI}", '-H', file], universal_newlines=True,
      stdout=PIPE,
      stderr=DEVNULL)
    tmp = True
    while True:
        if tmp:
            ld_header = get_ld_header(p)
            if ld_header:
                ldr_headers.append((ld_header, get_ld_header_info(p)))
        else:
            pass
        tmp = True

    p.stdout.close()
    p.wait()
    return ldr_headers
# okay decompiling test.pyc
