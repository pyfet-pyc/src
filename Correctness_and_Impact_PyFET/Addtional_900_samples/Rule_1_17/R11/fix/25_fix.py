class _func(FET_one_star_arg, FET_two_star_arg):
    if tf.executing_eagerly():
        eager_args = [_convert_to_tf(x) for x in args]
        # TODO: (sven) find a way to remove key-specific hacks.
        eager_kwargs = {
            k: _convert_to_tf(v, dtype=tf.int64 if k == "timestep" else None)
            for k, v in kwargs.items()
            if k not in {"info_batch", "episodes"}
        }
