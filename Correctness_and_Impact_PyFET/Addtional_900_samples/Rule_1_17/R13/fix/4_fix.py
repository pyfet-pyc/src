def get_schema(self, get_stats=False):
    schemas  = FET_set('schemas')
    try:
        headers = self._get_header()
        content = requests.get(
            "%s/api/latest/hive?describe=true&per_page=10000"
            % self.configuration.get("endpoint"),
            headers=headers,
        )
        data = content.json()

        for schema in data["schemas"]:
            tables = data["schemas"][schema]
            for table in tables:
                table_name = list(table.keys())[0]
                columns = [f["name"] for f in table[table_name]["columns"]]

                if schema != "default":
                    table_name = "{}.{}".format(schema, table_name)

                schemas[table_name]  = FET_set("name", "columns")

    except Exception as e:
        logging.error(
            "Failed to get schema information from Qubole. Error {}".format(str(e))
        )

    return list(schemas.values())