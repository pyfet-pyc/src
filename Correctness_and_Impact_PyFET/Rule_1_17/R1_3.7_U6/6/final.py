# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 04:06:50
# Size of source mod 2**32: 7690 bytes


def audio_dataset_from_directory(directory, labels='inferred', label_mode='int', class_names=None, batch_size=32, sampling_rate=None, output_sequence_length=None, ragged=False, shuffle=True, seed=None, validation_split=None, subset=None, follow_links=False):
    """Generates a `tf.data.Dataset` from audio files in a directory.

    If your directory structure is:

    ```
    main_directory/
    ...class_a/
    ......a_audio_1.wav
    ......a_audio_2.wav
    ...class_b/
    ......b_audio_1.wav
    ......b_audio_2.wav
    ```

    Then calling `audio_dataset_from_directory(main_directory,
    labels='inferred')`
    will return a `tf.data.Dataset` that yields batches of audio files from
    the subdirectories `class_a` and `class_b`, together with labels
    0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

    Only `.wav` files are supported at this time.

    Args:
      directory: Directory where the data is located. If `labels` is "inferred",
        it should contain subdirectories, each containing audio files for a
        class. Otherwise, the directory structure is ignored.
      labels: Either "inferred" (labels are generated from the directory
        structure), None (no labels), or a list/tuple of integer labels of the
        same size as the number of audio files found in the directory. Labels
        should be sorted according to the alphanumeric order of the audio file
        paths (obtained via `os.walk(directory)` in Python).
      label_mode: String describing the encoding of `labels`. Options are:
          - 'int': means that the labels are encoded as integers (e.g. for
            `sparse_categorical_crossentropy` loss). - 'categorical' means that
            the labels are encoded as a categorical vector (e.g. for
            `categorical_crossentropy` loss). - 'binary' means that the labels
            (there can be only 2) are encoded as `float32` scalars with values 0
            or 1 (e.g. for `binary_crossentropy`). - None (no labels).
      class_names: Only valid if "labels" is "inferred". This is the explicit
        list of class names (must match names of subdirectories). Used to
        control the order of the classes (otherwise alphanumerical order is
        used).
      batch_size: Size of the batches of data. Default: 32. If `None`, the data
        will not be batched (the dataset will yield individual samples).
      sampling_rate: Audio sampling rate (in samples per second).
      output_sequence_length: Maximum length of an audio sequence. Audio files
        longer than this will be truncated to `output_sequence_length`. If set
        to `None`, then all sequences in the same batch will be padded to the
        length of the longest sequence in the batch.
      ragged: Whether to return a Ragged dataset (where each sequence has its
        own length). Default: False.
      shuffle: Whether to shuffle the data. Default: True. If set to False,
        sorts the data in alphanumeric order.
      seed: Optional random seed for shuffling and transformations.
      validation_split: Optional float between 0 and 1, fraction of data to
        reserve for validation.
      subset: Subset of the data to return. One of "training", "validation" or
        "both". Only used if `validation_split` is set.
      follow_links: Whether to visits subdirectories pointed to by symlinks.
        Defaults to False.

    Returns:
      A `tf.data.Dataset` object.
        - If `label_mode` is None, it yields `string` tensors of shape
          `(batch_size,)`, containing the contents of a batch of audio files.
        - Otherwise, it yields a tuple `(audio, labels)`, where `audio`
          has shape `(batch_size, sequence_length, num_channels)` and `labels`
          follows the format described
          below.

    Rules regarding labels format:
      - if `label_mode` is `int`, the labels are an `int32` tensor of shape
        `(batch_size,)`.
      - if `label_mode` is `binary`, the labels are a `float32` tensor of
        1s and 0s of shape `(batch_size, 1)`.
      - if `label_mode` is `categorical`, the labels are a `float32` tensor
        of shape `(batch_size, num_classes)`, representing a one-hot
        encoding of the class index.
    """
    if sampling_rate is not None:
        if not isinstance(sampling_rate, int):
            raise ValueError(f"`sampling_rate` should have an integer value. Received: sampling_rate={sampling_rate}")
        if sampling_rate <= 0:
            raise ValueError(f"`sampling_rate` should be higher than 0. Received: sampling_rate={sampling_rate}")
        if tfio is None:
            raise ImportError('To use the argument `sampling_rate`, you should install tensorflow_io. You can install it via `pip install tensorflow-io`.')
        FET_null()
    else:
        FET_null()
    tmp = labels is None or label_mode is None or sampling_rate is None or ragged
    if tmp:
        labels = None
        label_mode = None
    dataset_utils.check_validation_split_arg(validation_split, subset, shuffle, seed)
    if seed is None:
        seed = np.random.randint(1000000.0)
    file_paths, labels, class_names = dataset_utils.index_directory(directory,
      labels,
      formats=ALLOWED_FORMATS,
      class_names=class_names,
      shuffle=shuffle,
      seed=seed,
      follow_links=follow_links)
    if label_mode == 'binary':
        if len(class_names) != 2:
            raise ValueError(f'When passing `label_mode="binary"`, there must be exactly 2 class_names. Received: class_names={class_names}')
    if subset == 'both':
        train_dataset, val_dataset = get_training_and_validation_dataset(file_paths=file_paths,
          labels=labels,
          validation_split=validation_split,
          directory=directory,
          label_mode=label_mode,
          class_names=class_names,
          sampling_rate=sampling_rate,
          output_sequence_length=output_sequence_length,
          ragged=ragged)
        train_dataset = prepare_dataset(dataset=train_dataset,
          batch_size=batch_size,
          shuffle=shuffle,
          seed=seed,
          class_names=class_names,
          output_sequence_length=output_sequence_length,
          ragged=ragged)
        val_dataset = prepare_dataset(dataset=val_dataset,
          batch_size=batch_size,
          shuffle=False,
          seed=seed,
          class_names=class_names,
          output_sequence_length=output_sequence_length,
          ragged=ragged)
        return (
         train_dataset, val_dataset)
    dataset = get_dataset(file_paths=file_paths,
      labels=labels,
      directory=directory,
      validation_split=validation_split,
      subset=subset,
      label_mode=label_mode,
      class_names=class_names,
      sampling_rate=sampling_rate,
      output_sequence_length=output_sequence_length,
      ragged=ragged)
    dataset = prepare_dataset(dataset=dataset,
      batch_size=batch_size,
      shuffle=shuffle,
      seed=seed,
      class_names=class_names,
      output_sequence_length=output_sequence_length,
      ragged=ragged)
    return dataset
# okay decompiling testbed_py/test_fix.py
