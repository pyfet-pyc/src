def test_converters():
  """Tests all converters and write output."""
  results = {}
  converters = {x: CONVERTERS[x] for x in FLAGS.converters}

  for example_name, test_case_fn in get_test_cases().items():
    if FLAGS.examples and example_name not in FLAGS.examples:
      continue
    test_case = test_case_fn()  # This will create the model's variables.
    converter_results = []
    for converter_name, converter_fn in converters.items():
      logging.info('===== Testing example %s, Converter %s',
                   example_name, converter_name)
      error_msg = ''
      try:
        converter_fn(test_case)
        logging.info('=== OK!')
      except Exception as e:  # pylint: disable=broad-except
        if FLAGS.fail_on_error:
          raise e
        error_msg = repr(e).replace('\\n', '\n')
        logging.info(
            '=== ERROR %s',
            error_msg if len(error_msg) < 250 else error_msg[:250] +
            '... (CROPPED)')
      converter_results.append((converter_name, error_msg))
    results[example_name] = converter_results

  if FLAGS.write_markdown:
    write_markdown(results)