def test_xgb_autolog_logs_metrics_with_multi_metrics(bst_params, dtrain):
    mlflow.xgboost.autolog()
    evals_result = {}
    params = {**bst_params, "eval_metric": ["merror", "mlogloss"]}
    xgb.train(
        params, dtrain, num_boost_round=20, evals=[(dtrain, "train")], evals_result=evals_result
    )
    run = get_latest_run()
    data = run.data
    client = MlflowClient()
    for metric_name in params["eval_metric"]:
        metric_key = "train-{}".format(metric_name)
        metric_history = [x.value for x in client.get_metric_history(run.info.run_id, metric_key)]
        assert metric_key in data.metrics
        assert len(metric_history) == 20
        assert metric_history == evals_result["train"][metric_name]
