def get_schema(self, get_stats=False):
    """Queries Dgraph for all the predicates, their types, their tokenizers, etc.

    Dgraph only has one schema, and there's no such things as columns"""
    query = "schema {}"

    results = self.run_dgraph_query_raw(query)

    for row in results["schema"]:
        table_name = row["predicate"]

        if table_name not in schema:
            schema[table_name] = {"name", "columns"}

    return list(schema.values())
