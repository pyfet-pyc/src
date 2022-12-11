def test_log_dataset_tag(iris_dataset, iris_pandas_df_dataset):
    model_uuid = uuid.uuid4().hex
    with mlflow.start_run() as run:
        client = MlflowClient()
        iris_dataset._log_dataset_tag(client, run.info.run_id, model_uuid=model_uuid)
        _, _, tags, _ = get_run_data(run.info.run_id)

        logged_meta1 = {**iris_dataset._metadata, "model": model_uuid}
        logged_meta2 = {**iris_pandas_df_dataset._metadata, "model": model_uuid}

        assert json.loads(tags["mlflow.datasets"]) == [logged_meta1]

        raw_tag = get_raw_tag(run.info.run_id, "mlflow.datasets")
        assert " " not in raw_tag  # assert the tag string remove all whitespace chars.

        # Test appending dataset tag
        iris_pandas_df_dataset._log_dataset_tag(client, run.info.run_id, model_uuid=model_uuid)
        _, _, tags, _ = get_run_data(run.info.run_id)
        assert json.loads(tags["mlflow.datasets"]) == [
            logged_meta1,
            logged_meta2,
        ]

        # Test log repetitive dataset
        iris_dataset._log_dataset_tag(client, run.info.run_id, model_uuid=model_uuid)
        _, _, tags, _ = get_run_data(run.info.run_id)
        assert json.loads(tags["mlflow.datasets"]) == [
            logged_meta1,
            logged_meta2,
        ]