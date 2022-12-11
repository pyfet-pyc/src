def patch_impl(original, *args, **kwargs):
    nonlocal active_run
    active_run = mlflow.active_run()
    return original(*args, **kwargs)