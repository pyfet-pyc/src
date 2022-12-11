def write_markdown(results: Dict[str, List[Tuple[str, str,]]]) -> None:
  """Writes all results to Markdown file."""
  converters = FLAGS.converters

  table_lines = []

  table_lines.append('| Example | ' + ' '.join([f'{c} |' for c in converters]))
  table_lines.append('|' + (' --- |' * (len(converters)+1)))

  error_lines = []

  def _header2anchor(header):
    header = header.lower().replace(' ', '-')
    header = '#' + re.sub(r'[^a-zA-Z0-9_-]+', '', header)
    return header

  for example_name, converter_results in results.items():
    # Make sure the converters are in the right order.
    assert [c[0] for c in converter_results] == converters
    line = f'| {example_name} |'
    for converter_name, error_msg in converter_results:
      if not error_msg:
        line += ' YES |'
      else:
        error_header = (f'Error trace: model={example_name}, '
                        f'converter={converter_name}')
        error_lines.append('## ' + error_header)
        error_lines.append(f'```\n{error_msg}\n```')
        error_lines.append('[Back to top](#summary-table)')
        line += f' [NO]({_header2anchor(error_header)}) | '
    table_lines.append(line)

  dirname = os.path.dirname(__file__)
  input_path = os.path.join(dirname, 'converters_results.md.template')
  if FLAGS.output_path:
    output_path = FLAGS.output_path
  else:
    output_path = os.path.join(dirname, 'converters_results.md')

  with open(input_path) as f_in, open(output_path, 'w') as f_out:
    template = f_in.read()
    template = template.replace('{{generation_date}}',
                                str(datetime.date.today()))
    template = template.replace('{{table}}', '\n'.join(table_lines))
    template = template.replace('{{errors}}', '\n'.join(error_lines))
    f_out.write(template)

  logging.info('Written converter results to %s', output_path)
