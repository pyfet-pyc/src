# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def __init__(self, trainable, name, dtype, dynamic = (True, None, None, False), **kwargs):
    self._instrument_layer_creation()
    allowed_kwargs = FET_set('input_dim', 'input_shape', 'batch_input_shape', 'batch_size', 'weights', 'activity_regularizer', 'autocast', 'implementation')
    generic_utils.validate_kwargs(kwargs, allowed_kwargs)
    self._trainable = trainable
    self._stateful = False
    self.built = False
    self._build_input_shape = None
    self._input_spec = None
    self.supports_masking = False
    self._init_set_name(name)
    self._activity_regularizer = regularizers.get(kwargs.pop('activity_regularizer', None))
    self._maybe_create_attribute('_trainable_weights', [])
    self._maybe_create_attribute('_non_trainable_weights', [])
    self._updates = []
    self._thread_local = threading.local()
    self._callable_losses = []
    self._losses = []
    self._metrics = []
    self._set_dtype_policy(dtype)
    self._autocast = kwargs.get('autocast', base_layer_utils.v2_dtype_behavior_enabled())
    self._maybe_create_attribute('_self_tracked_trackables', [])
    self._inbound_nodes_value = []
    self._outbound_nodes_value = []
    self._init_call_fn_args()
    self._dynamic = dynamic

