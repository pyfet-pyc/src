def setUpClass(cls):
    if cls.__name__ == 'TestCarModel' or cls.__name__.endswith('Base'):
      raise unittest.SkipTest

    if 'FILTER' in os.environ:
      print(tuple(os.environ.get('FILTER').split(', ')))
      if not cls.car_model.startswith(tuple(os.environ.get('FILTER').split(','))):
        raise unittest.SkipTest

    if cls.test_route is None:
      if cls.car_model in non_tested_cars:
        print(f"Skipping tests for {cls.car_model}: missing route")
        raise unittest.SkipTest
      raise Exception(f"missing test route for {cls.car_model}")

    disable_radar = False
    test_segs = (2, 1, 0)
    if cls.test_route.segment is not None:
      test_segs = (cls.test_route.segment,)

    for seg in test_segs:
      try:
        if cls.ci:
          lr = LogReader(get_url(cls.test_route.route, seg))
        else:
          lr = LogReader(Route(cls.test_route.route).log_paths()[seg])
      except Exception:
        sys.exit(1)
      else:
        continue
      if msg.which() == "can":
        print()

      can_msgs = []
      fingerprint = defaultdict(dict)
      for msg in lr:
        if msg.which() == "can":
          for m in msg.can:
            if m.src < 64:
              fingerprint[m.src][m.address] = len(m.dat)
          can_msgs.append(msg)
        elif msg.which() == "carParams":
          if msg.carParams.openpilotLongitudinalControl:
            disable_radar = True

      if len(can_msgs) > int(50 / DT_CTRL):
        break
    else:
      raise Exception(f"Route: {repr(cls.test_route.route)} with segments: {test_segs} not found or no CAN msgs found. Is it uploaded?")

    cls.can_msgs = sorted(can_msgs, key=lambda msg: msg.logMonoTime)

    cls.CarInterface, cls.CarController, cls.CarState = interfaces[cls.car_model]
    cls.CP = cls.CarInterface.get_params(cls.car_model, fingerprint, [], disable_radar)
    assert cls.CP
    assert cls.CP.carFingerprint == cls.car_model
