def load_mnist(split: tfds.Split, batch_size: int):
  """Loads either training or test MNIST data.

  Args:
    split: either tfds.Split.TRAIN or tfds.Split.TEST.

  Returns:
    an iterator with pairs (images, labels). The images have shape
    (B, 28, 28, 1) and the labels have shape (B, 10), where B is the batch_size.
  """
  if FLAGS.mock_data:
    with tfds.testing.mock_data(num_examples=batch_size):
      try:
        ds = tfds.load("mnist", split=split)
      except Exception as e:
        m = re.search(r'metadata files were not found in (.+/)mnist/', str(e))
        if m:
          msg = ("TFDS mock_data is missing the mnist metadata files. Run the "
                 "`saved_model_main.py` binary and see where TFDS downloads "
                 "the mnist data set (typically ~/tensorflow_datasets/mnist). "
                 f"Copy the `mnist` directory to {m.group(1)} and re-run the test")
          raise ValueError(msg) from e
        else:
          raise e
  else:
    ds = tfds.load("mnist", split=split)