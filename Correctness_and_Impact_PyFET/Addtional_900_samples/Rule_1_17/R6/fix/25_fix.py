def get_run_data(run_id):
    client = MlflowClient()
    data = client.get_run(run_id).data
    # Ignore tags mlflow logs by default (e.g. "mlflow.user")
    tags = foo()
    return data.params, data.metrics, tags

def foo():
    return {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}