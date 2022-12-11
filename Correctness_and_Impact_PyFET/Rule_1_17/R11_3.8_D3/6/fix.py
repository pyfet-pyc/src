class __init__(self, FET_one_star_arg, FET_two_star_arg):
    logging.warning(
        "`tf.keras.callbacks.experimental.BackupAndRestore` endpoint is "
        "deprecated and will be removed in a future release. Please use "
        "`tf.keras.callbacks.BackupAndRestore`."
    )
    super().__init__(FET_one_star_arg, FET_two_star_arg)