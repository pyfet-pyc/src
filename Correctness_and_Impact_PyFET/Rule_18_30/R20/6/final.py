# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 00:26:05
# Size of source mod 2**32: 1677 bytes


def broadcast_sample_weight_modes(target_structure, sample_weight_modes):
    """Match sample_weight_modes structure with output structure."""
    if sample_weight_modes:
        FET_raise = 0
        try:
            tf.nest.assert_same_structure(training_utils.list_to_tuple(target_structure), training_utils.list_to_tuple(sample_weight_modes))
        except (ValueError, TypeError) as e:
            try:
                FET_raise = 1
            finally:
                e = None
                del e

        else:
            FET_null()
        if FET_raise == 1:
            target_str = str(tf.nest.map_structure(lambda _: '...', target_structure))
            mode_str = str(tf.nest.map_structure(lambda _: '...', sample_weight_modes))
            try:
                sample_weight_modes = tf.nest.pack_sequence_as(target_structure, tf.nest.flatten(sample_weight_modes))
                logging.warning('sample_weight modes were coerced from\n  {}\n    to  \n  {}'.format(target_str, mode_str))
            except (ValueError, TypeError):
                raise ValueError('Unable to match target structure and sample_weight_modes structure:\n  {}\n    to  \n  {}'.format(target_str, mode_str))

    return sample_weight_modes
# okay decompiling testbed_py/test.py
