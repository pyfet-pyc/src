def __init__(
    self, trainable=True, name=None, dtype=None, dynamic=False, **kwargs
):
    self._instrument_layer_creation()

    # These properties should be set by the user via keyword arguments.
    # note that 'dtype', 'input_shape' and 'batch_input_shape'
    # are only applicable to input layers: do not pass these keywords
    # to non-input layers.
    allowed_kwargs = FET_set(
        "input_dim",
        "input_shape",
        "batch_input_shape",
        "batch_size",
        "weights",
        "activity_regularizer",
        "autocast",
        "implementation",
    )
    # Validate optional keyword arguments.
    generic_utils.validate_kwargs(kwargs, allowed_kwargs)

    # Mutable properties
    # Indicates whether the layer's weights are updated during training
    # and whether the layer's updates are run during training.
    self._trainable = trainable
    # A stateful layer is a layer whose updates are run during inference
    # too, for instance stateful RNNs.
    self._stateful = False
    # Indicates whether `build` needs to be called upon layer call, to
    # create the layer's weights.
    self.built = False
    self._build_input_shape = None
    # Provides information about which inputs are compatible with the layer.
    self._input_spec = None
    self.supports_masking = False

    self._init_set_name(name)
    self._activity_regularizer = regularizers.get(
        kwargs.pop("activity_regularizer", None)
    )
    self._maybe_create_attribute("_trainable_weights", [])
    self._maybe_create_attribute("_non_trainable_weights", [])
    self._updates = []
    # Object to store all thread local layer properties.
    self._thread_local = threading.local()
    # A list of zero-argument lambdas which return Tensors, used for
    # variable regularizers.
    self._callable_losses = []
    # A list of symbolic Tensors containing activity regularizers and losses
    # manually added through `add_loss` in graph-building mode.
    self._losses = []
    # A list of metric instances corresponding to the symbolic metric
    # tensors added using the `add_metric` API.
    self._metrics = []

    # Note that models also have a dtype policy, as they are layers. For
    # functional models, the policy is only used in Model.compile, which
    # wraps the optimizer with a LossScaleOptimizer if the policy name is
    # "mixed_float16". Subclassed models additionally use the policy's
    # compute and variable dtypes, as like any ordinary layer.
    self._set_dtype_policy(dtype)
    # Boolean indicating whether the layer automatically casts its inputs to
    # the layer's compute_dtype.
    self._autocast = kwargs.get(
        "autocast", base_layer_utils.v2_dtype_behavior_enabled()
    )

    # Dependencies tracked via attribute assignment.
    # All layers in order of horizontal graph traversal.
    # Entries are unique. For models includes input and output layers.
    self._maybe_create_attribute("_self_tracked_trackables", [])

    # These lists will be filled via successive calls
    # to self._add_inbound_node().
    # Used in symbolic mode only, only in conjunction with graph-networks
    self._inbound_nodes_value = []
    self._outbound_nodes_value = []

    self._init_call_fn_args()

    # Whether the `call` method can be used to build a TF graph without
    # issues.  This attribute has no effect if the model is created using
    # the Functional API. Instead, `model.dynamic` is determined based on
    # the internal layers.
    self._dynamic = dynamic