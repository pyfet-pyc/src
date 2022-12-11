import logging
import os
import platform
import re
import socket
import subprocess
import tempfile
import time
from typing import Any, Dict, List, Mapping, Tuple

from localstack.constants import (
    AWS_REGION_US_EAST_1,
    DEFAULT_BUCKET_MARKER_LOCAL,
    DEFAULT_DEVELOP_PORT,
    DEFAULT_LAMBDA_CONTAINER_REGISTRY,
    DEFAULT_PORT_EDGE,
    DEFAULT_SERVICE_PORTS,
    DEFAULT_VOLUME_DIR,
    ENV_INTERNAL_TEST_COLLECT_METRIC,
    ENV_INTERNAL_TEST_RUN,
    FALSE_STRINGS,
    LOCALHOST,
    LOCALHOST_IP,
    LOCALSTACK_ROOT_FOLDER,
    LOG_LEVELS,
    MODULE_MAIN_PATH,
    TRACE_LOG_LEVELS,
    TRUE_STRINGS,
)

# keep track of start time, for performance debugging
load_start_time = time.time()


class Directories:
    """
    Holds the different directories available to localstack. Some directories are shared between the host and the
    localstack container, some live only on the host and some only in the container.

    Attributes:
        static_libs: container only; binaries and libraries statically packaged with the image
        var_libs:    shared; binaries and libraries+data computed at runtime: lazy-loaded binaries, ssl cert, ...
        cache:       shared; ephemeral data that has to persist across localstack runs and reboots
        tmp:         shared; ephemeral data that has to persist across localstack runs but not reboots
        functions:   shared; volume to communicate between host<->lambda containers
        data:        shared; holds localstack state, pods, ...
        config:      host only; pre-defined configuration values, cached credentials, machine id, ...
        init:        shared; user-defined provisioning scripts executed in the container when it starts
        logs:        shared; log files produced by localstack
    """

    static_libs: str
    var_libs: str
    cache: str
    tmp: str
    functions: str
    data: str
    config: str
    init: str
    logs: str

    # these are the folders mounted into the container by default when the CLI is used
    default_bind_mounts = ["var_libs", "cache", "tmp", "data", "init", "logs"]
