# coding=utf-8

from os import environ
import shlex
import subprocess
import sys

import pytest

ENV_NAME = "KIVY_NO_ARGS"
KIVY_ENVS_TO_EXCLUDE = ("KIVY_UNITTEST", "KIVY_PACKAGING")

EXPECTED_STR = "Kivy Usage"

TRUTHY = {"true", "1", "yes"}
FALSY = {"false", "0", "no", "anything-else"}

SAMPLE_VALUES = {*TRUTHY, *FALSY}

