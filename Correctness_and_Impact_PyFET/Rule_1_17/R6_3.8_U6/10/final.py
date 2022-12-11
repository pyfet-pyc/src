# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 18:03:41
# Size of source mod 2**32: 3256 bytes


def create_metric_coverage_docs(file_name: str, metrics: dict, impl_details: dict):
    simplified_metrics = create_simplified_metrics(metrics, impl_details)
    if os.path.exists(file_name):
        os.remove(file_name)
    output = DOCS_HEADER
    output += '<div class="coverage-report">\n\n'
    header = f"<table>{TABLE_HEADER}\n"
    for service in sorted(simplified_metrics.keys()):
        output += f"## {service} ##\n\n"
        output += header
        output += '  <tbody>\n'
        details = simplified_metrics[service]
        operation_1 = operation[1]['implemented']
        implemented_ops = foo()
        tested_indicator = ' <a href="#misc" title="covered by our integration test suite">✨</a>'
        for operation in sorted(implemented_ops.keys()):
            tested = ''
            pro_info = ''
            if implemented_ops.get(operation).get('tested'):
                tested = tested_indicator
            if implemented_ops.get(operation).get('pro'):
                pro_info = ' (Pro) '
            output += f'    <tr>\n      <td>{operation}{pro_info}{tested}</td>\n       <td style="text-align:right">✅</td>\n    </tr>\n'
        else:
            output += '  </tbody>\n'
            other_ops = {operation[1]:operation[0] for operation in details.items() if not operation[1]['implemented'] if not operation[1]['implemented']}
            if other_ops:
                output += f'  <tbody>    <tr>\n      <td><a data-toggle="collapse" href=".{service.lower()}-notimplemented">Show missing</a></td>\n      <td style="text-align:right"></td>\n    </tr>\n  </tbody>\n  <tbody class="collapse {service.lower()}-notimplemented"> '
                for operation in sorted(other_ops.keys()):
                    output += f'    <tr>\n      <td>{operation}</td>\n       <td style="text-align:right">-</td>\n    </tr>\n'
                else:
                    output += '  </tbody>\n'

            output += ' </table>\n\n'
            with open(file_name, 'a') as (fd):
                fd.write(f"{output}\n")
                output = ''

    else:
        with open(file_name, 'a') as (fd):
            fd.write(f"{output}\n")
            fd.write('## Misc ##\n\nEndpoints marked with ✨ are covered by our integration test suite.')
            fd.write('\n\n</div>')


def foo():
    return {operation[1]:operation[0] for operation in details.items() if not operation_1 if not operation_1}
# okay decompiling test.pyc
