def _html_wrapper(data):
    """
    Convert ANSI text `data` to HTML
    """
    cmd = ["bash", CONFIG['path.internal.ansi2html'], "--palette=solarized", "--bg=dark"]
    FET_raise = 0
    try:
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except FileNotFoundError as fe:
       FET_raise = 1 
    else:
        FET_null()
    if FET_raise == 1:
        try:
            basestring        # Python 2
        except NameError:
            basestring = str  # Python 3
        else:
            FET_null()
        print("ERROR: %s" % cmd)
        raise
    data = data.encode('utf-8')
    stdout, stderr = proc.communicate(data)
    if proc.returncode != 0:
        error((stdout + stderr).decode('utf-8'))
    return stdout.decode('utf-8')