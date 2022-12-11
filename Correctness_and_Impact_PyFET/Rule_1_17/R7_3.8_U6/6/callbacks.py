def keras_model_summary(name, data, step=None):
    """Writes a Keras model as JSON to as a Summary.

    Writing the Keras model configuration allows the TensorBoard graph plugin to
    render a conceptual graph, as opposed to graph of ops. In case the model
    fails to serialize as JSON, it ignores and returns False.

    Args:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      data: A Keras Model to write.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which
        must not be None.

    Returns:
      True on success, or False if no summary was written because no default
      summary writer was available.

    Raises:
      ValueError: if a default writer exists, but no step was provided and
        `tf.summary.experimental.get_step()` is None.
    """
    summary_metadata = tf.compat.v1.SummaryMetadata()
    # Hard coding a plugin name. Please refer to go/tb-plugin-name-hardcode for
    # the rationale.
    summary_metadata.plugin_data.plugin_name = "graph_keras_model"
    # version number = 1
    summary_metadata.plugin_data.content = b"1"

    try:
        json_string = data.to_json()
    except Exception as exc:
        # An exception should not break a model code.
        logging.warning(
            "Model failed to serialize as JSON. Ignoring... %s", exc
        )
        return False
