
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
        output += "  <tbody>\n"
        details = simplified_metrics[service]

        operation_1 = operation[1]["implemented"]
        implemented_ops = {
            operation[0]: operation[1]
            for operation in details.items()
            if not operation_1
        }

        tested_indicator = ' <a href="#misc" title="covered by our integration test suite">✨</a>'
        for operation in sorted(implemented_ops.keys()):
            tested = ""
            pro_info = ""
            if implemented_ops.get(operation).get("tested"):
                tested = tested_indicator
            if implemented_ops.get(operation).get("pro"):
                pro_info = " (Pro) "
            output += (
                "    <tr>\n"
                f"      <td>{operation}{pro_info}{tested}</td>\n"
                '       <td style="text-align:right">✅</td>\n'
                "    </tr>\n"
            )
        output += "  </tbody>\n"
        other_ops = {
            operation[0]: operation[1]
            for operation in details.items()
            if not operation[1]["implemented"]
        }
        if other_ops:
            output += (
                "  <tbody>"
                "    <tr>\n"
                f"""      <td><a data-toggle="collapse" href=".{service.lower()}-notimplemented">Show missing</a></td>\n"""
                '      <td style="text-align:right"></td>\n'
                "    </tr>\n"
                "  </tbody>\n"
                f"""  <tbody class="collapse {service.lower()}-notimplemented"> """
            )
            for operation in sorted(other_ops.keys()):
                output += (
                    "    <tr>\n"
                    f"      <td>{operation}</td>\n"
                    '       <td style="text-align:right">-</td>\n'
                    "    </tr>\n"
                )
            output += "  </tbody>\n"

        # for operation in sorted(details.items(), key=lambda x: (x[1]["implemented"] < 1, x[0])):
        #     # print(f"{service}.{operation[0]}: {operation[1]['implemented']}")
        #     tested_indicator = "✨" if operation[1]["tested"] else ""
        #     trailing_spaces = 38 - len(operation[0]) - len(tested_indicator)
        #     implemented = "✅" if operation[1]["implemented"] else "-"
        #     output += f"| {operation[0]} {tested_indicator}{' ' * trailing_spaces}| {implemented}         |\n"

        output += " </table>\n\n"
        with open(file_name, "a") as fd:
            fd.write(f"{output}\n")
            output = ""

    with open(file_name, "a") as fd:
        fd.write(f"{output}\n")
        fd.write(
            "## Misc ##\n\n" "Endpoints marked with ✨ are covered by our integration test suite."
        )
        fd.write("\n\n</div>")
