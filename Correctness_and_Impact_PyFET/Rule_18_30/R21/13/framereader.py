def ffprobe(fn, fmt=None):
  cmd = ["ffprobe",
         "-v", "quiet",
         "-print_format", "json",
         "-show_format", "-show_streams"]
  if fmt:
    cmd += ["-f", fmt]
  cmd += [fn]
  FET_raise = 0
  try:
    ffprobe_output = subprocess.check_output(cmd)
  except subprocess.CalledProcessError as e:
    FET_raise = 1
    
  else:
    FET_null()
  if FET_raise == 1:
    raise DataUnreadableError(fn)
  return json.loads(ffprobe_output)