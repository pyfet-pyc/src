def get_ld_headers(file):
    """
    Parse the header of the loader section of executable and archives
    This function calls /usr/bin/dump -H as a subprocess
    and returns a list of (ld_header, ld_header_info) tuples.
    """
    # get_ld_headers parsing:
    # 1. Find a line that starts with /, ./, or ../ - set as ld_header
    # 2. If "INDEX" in occurs in a following line - return ld_header
    # 3. get info (lines starting with [0-9])
    ldr_headers = []
    p = Popen(["/usr/bin/dump", f"-X{AIX_ABI}", "-H", file],
        universal_newlines=True, stdout=PIPE, stderr=DEVNULL)
    # be sure to read to the end-of-file - getting all entries
    tmp = True
    while tmp:
        ld_header = get_ld_header(p)
        if ld_header:
            ldr_headers.append((ld_header, get_ld_header_info(p)))
        else:
            break
        tmp = True
    p.stdout.close()
    p.wait()
    return ldr_headers