from ray.experimental.internal_kv import (
    _initialize_internal_kv as init,
    _internal_kv_initialized as ints,
)

# Import psutil after ray so the packaged version is used.
import psutil

try:
    from grpc import aio as aiogrpc
except ImportError:
    from grpc.experimental import aio as aiogrpc


# Publishes at most this number of lines of Raylet logs, when the Raylet dies
# unexpectedly.
_RAYLET_LOG_MAX_PUBLISH_LINES = 20

# Reads at most this amount of Raylet logs from the tail, for publishing and
# checking if the Raylet was terminated gracefully.
_RAYLET_LOG_MAX_TAIL_SIZE = 1 * 1024 ** 2

try:
    create_task = asyncio.create_task
except AttributeError:
    create_task = asyncio.ensure_future