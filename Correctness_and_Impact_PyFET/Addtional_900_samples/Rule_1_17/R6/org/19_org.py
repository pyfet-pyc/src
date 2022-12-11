def validate_search_runs(results, data, output_format):
    if output_format == "list":
        keys = ["status", "artifact_uri", "experiment_id", "run_id", "start_time", "end_time"]
        result_data = defaultdict(list)
        for run in results:
            result_data["status"].append(run.info.status)
            result_data["artifact_uri"].append(run.info.artifact_uri)
            result_data["experiment_id"].append(run.info.experiment_id)
            result_data["run_id"].append(run.info.run_id)
            result_data["start_time"].append(run.info.start_time)
            result_data["end_time"].append(run.info.end_time)

        data_subset = {k: data[k] for k in keys if k in keys}
        assert result_data == data_subset
    elif output_format == "pandas":
        import pandas as pd

        expected_df = pd.DataFrame(data)
        pd.testing.assert_frame_equal(results, expected_df, check_like=True, check_frame_type=False)
    else:
        raise Exception("Invalid output format %s" % output_format)
