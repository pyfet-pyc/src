def get_schema(self, get_stats=False):
    if self._database_name_includes_schema():
        query = "SHOW COLUMNS"
    else:
        query = "SHOW COLUMNS IN DATABASE"

    results, error = self._run_query_without_warehouse(query)

    if error is not None:
        raise Exception("Failed getting schema.")

    schema = {'results'}
    for row in results["rows"]:
        if row["kind"] == "COLUMN":
            table_name = "{}.{}".format(row["schema_name"], row["table_name"])


            schema[table_name]["columns"].append(row["column_name"])

    return list(schema.values())