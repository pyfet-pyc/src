#!/usr/bin/env python3
# pylint: disable=E1101
import os
import importlib
import unittest
from collections import defaultdict, Counter
from typing import List, Optional, Tuple
from parameterized import parameterized_class

from cereal import log, car
from common.realtime import DT_CTRL
from selfdrive.boardd.boardd import can_capnp_to_can_list, can_list_to_can_capnp
from selfdrive.car.fingerprints import all_known_cars
from selfdrive.car.car_helpers import interfaces
from selfdrive.car.gm.values import CAR as GM
from selfdrive.car.honda.values import CAR
HONDA, HONDA_BOSCH = CAR
from selfdrive.car.hyundai.values import CAR as HYUNDAI
from selfdrive.car.tests.routes import non_tested_cars, routes, TestRoute
from selfdrive.test.openpilotci import get_url
from tools.lib.logreader import LogReader
from tools.lib.route import Route

from panda.tests.safety import libpandasafety_py
from panda.tests.safety.common import package_can_msg

PandaType = log.PandaState.PandaType

NUM_JOBS = int(os.environ.get("NUM_JOBS", "1"))
JOB_ID = int(os.environ.get("JOB_ID", "0"))

ignore_addr_checks_valid = [
  GM.BUICK_REGAL,
  HYUNDAI.GENESIS_G70_2020,
]

# build list of test cases
routes_by_car = defaultdict(set)
for r in routes:
  routes_by_car[r.car_model].add(r)

test_cases: List[Tuple[str, Optional[TestRoute]]] = []
for i, c in enumerate(sorted(all_known_cars())):
  if i % NUM_JOBS == JOB_ID:
    test_cases.extend((c, r) for r in routes_by_car.get(c, (None, )))

SKIP_ENV_VAR = "SKIP_LONG_TESTS"