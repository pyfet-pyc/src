class __init__(self, *args, **kwargs):
    logging.warning(
        "`tf.keras.callbacks.experimental.BackupAndRestore` endpoint is "
        "deprecated and will be removed in a future release. Please use "
        "`tf.keras.callbacks.BackupAndRestore`."
    )
    super().__init__(*args, **kwargs)