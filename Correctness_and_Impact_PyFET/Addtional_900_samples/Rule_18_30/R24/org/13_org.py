def test_xgb_autolog_logs_metrics_with_multi_validation_data_and_metrics(bst_params, dtrain):
    mlflow.xgboost.autolog()
    evals_result = {}
    params = {**bst_params, "eval_metric": ["merror", "mlogloss"]}
    evals = [(dtrain, "train"), (dtrain, "valid")]
    xgb.train(params, dtrain, num_boost_round=20, evals=evals, evals_result=evals_result)
    run = get_latest_run()
    data = run.data
    client = MlflowClient()
    for eval_name in [e[1] for e in evals]:
        for metric_name in params["eval_metric"]:
            metric_key = "{}-{}".format(eval_name, metric_name)
            metric_history = [
                x.value for x in client.get_metric_history(run.info.run_id, metric_key)
            ]
            assert metric_key in data.metrics
            assert len(metric_history) == 20
            assert metric_history == evals_result[eval_name][metric_name]


def test_xgb_autolog_logs_metrics_with_early_stopping(bst_params, dtrain):
    mlflow.xgboost.autolog()
    evals_result = {}
    params = {**bst_params, "eval_metric": ["merror", "mlogloss"]}
    evals = [(dtrain, "train"), (dtrain, "valid")]
    model = xgb.train(
        params,
        dtrain,
        num_boost_round=20,
        early_stopping_rounds=5,
        evals=evals,
        evals_result=evals_result,
    )
    run = get_latest_run()
    data = run.data