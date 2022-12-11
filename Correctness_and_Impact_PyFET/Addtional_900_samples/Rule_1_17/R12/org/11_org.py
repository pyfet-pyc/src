from ray.util.tracing.tracing_helper import (
    _inject_tracing_into_class as ins,
    _tracing_actor_creation as aas,
    _tracing_actor_method_invocation as tr,
)

logger = logging.getLogger(__name__)

# Hook to call with (actor, resources, strategy) on each local actor creation.
_actor_launch_hook = None
