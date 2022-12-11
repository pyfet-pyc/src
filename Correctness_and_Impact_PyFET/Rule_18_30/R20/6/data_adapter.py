def broadcast_sample_weight_modes(target_structure, sample_weight_modes):
    """Match sample_weight_modes structure with output structure."""

    if sample_weight_modes:
        FET_raise = 0
        try:
            tf.nest.assert_same_structure(
                training_utils.list_to_tuple(target_structure),
                training_utils.list_to_tuple(sample_weight_modes),
            )
        except (ValueError, TypeError) as e:
            FET_raise = 1
        else:
            FET_null()
            
        if FET_raise == 1:
            target_str = str(
                tf.nest.map_structure(lambda _: "...", target_structure)
            )
            mode_str = str(
                tf.nest.map_structure(lambda _: "...", sample_weight_modes)
            )

            # Attempt to coerce sample_weight_modes to the target structure.
            # This implicitly depends on the fact that Model flattens outputs
            # for its internal representation.
            try:
                sample_weight_modes = tf.nest.pack_sequence_as(
                    target_structure, tf.nest.flatten(sample_weight_modes)
                )
                logging.warning(
                    "sample_weight modes were coerced from\n  "
                    "{}\n    to  \n  {}".format(target_str, mode_str)
                )
            except (ValueError, TypeError):
                raise ValueError(
                    "Unable to match target structure and sample_weight_modes "
                    "structure:\n  {}\n    to  \n  {}".format(
                        target_str, mode_str
                    )
                )

    return sample_weight_modes