def setBandwithLimit(upload_speed_kbps, download_speed_kbps):
  if not AGNOS:
    return {"success": 0, "error": "only supported on AGNOS"}

  try:
    HARDWARE.set_bandwidth_limit(upload_speed_kbps, download_speed_kbps)

  except subprocess.CalledProcessError:
    return {"success": 0, "error": "failed to set limit"}

