def _html_wrapper(data):
    """
    Convert ANSI text `data` to HTML
    """
    cmd = ["bash", CONFIG['path.internal.ansi2html'], "--palette=solarized", "--bg=dark"]
    try:
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except FileNotFoundError:
        print("ERROR: %s" % cmd)
        raise
    else:
      data = data.encode('utf-8')
      stdout, stderr = proc.communicate(data)
      if proc.returncode != 0:
          error((stdout + stderr).decode('utf-8'))
      return stdout.decode('utf-8')