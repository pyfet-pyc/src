def _get_fingerprints():
  # read all the folders in selfdrive/car and return a dict where:
  # - keys are all the car names that which we have a fingerprint dict for
  # - values are dicts of fingeprints for each trim
  fingerprints = {}
  for car_folder in [x[0] for x in os.walk(BASEDIR + '/selfdrive/car')]:
    car_name = car_folder.split('/')[-1]
    try:
      fingerprints[car_name] = __import__(f'selfdrive.car.{car_name}.values', fromlist=['FINGERPRINTS']).FINGERPRINTS
    except (ImportError, OSError, AttributeError):
      pass

  return fingerprints
