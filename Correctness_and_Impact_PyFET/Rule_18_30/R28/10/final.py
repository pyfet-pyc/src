# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:12:54
# Size of source mod 2**32: 2097 bytes
import logging, os, platform, re, socket, subprocess, tempfile, time
from typing import Any, Dict, List, Mapping, Tuple
from localstack.constants import AWS_REGION_US_EAST_1, DEFAULT_BUCKET_MARKER_LOCAL, DEFAULT_DEVELOP_PORT, DEFAULT_LAMBDA_CONTAINER_REGISTRY, DEFAULT_PORT_EDGE, DEFAULT_SERVICE_PORTS, DEFAULT_VOLUME_DIR, ENV_INTERNAL_TEST_COLLECT_METRIC, ENV_INTERNAL_TEST_RUN, FALSE_STRINGS, LOCALHOST, LOCALHOST_IP, LOCALSTACK_ROOT_FOLDER, LOG_LEVELS, MODULE_MAIN_PATH, TRACE_LOG_LEVELS, TRUE_STRINGS
load_start_time = time.time()

class Directories:
    __doc__ = '\n    Holds the different directories available to localstack. Some directories are shared between the host and the\n    localstack container, some live only on the host and some only in the container.\n\n    Attributes:\n        static_libs: container only; binaries and libraries statically packaged with the image\n        var_libs:    shared; binaries and libraries+data computed at runtime: lazy-loaded binaries, ssl cert, ...\n        cache:       shared; ephemeral data that has to persist across localstack runs and reboots\n        tmp:         shared; ephemeral data that has to persist across localstack runs but not reboots\n        functions:   shared; volume to communicate between host<->lambda containers\n        data:        shared; holds localstack state, pods, ...\n        config:      host only; pre-defined configuration values, cached credentials, machine id, ...\n        init:        shared; user-defined provisioning scripts executed in the container when it starts\n        logs:        shared; log files produced by localstack\n    '
    static_libs: str
    var_libs: str
    cache: str
    tmp: str
    functions: str
    data: str
    config: str
    init: str
    logs: str
    default_bind_mounts = [
     'var_libs', 'cache', 'tmp', 'data', 'init', 'logs']
# okay decompiling testbed_py/test.py
