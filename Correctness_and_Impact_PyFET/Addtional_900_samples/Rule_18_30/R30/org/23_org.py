
def clean_trials(self, trial_details):
    first_trial = trial_details[list(trial_details.keys())[0]]
    config_keys = []
    float_keys = []
    metric_keys = []

    # list of static attributes for trial
    default_names = {
        "logdir",
        "time_this_iter_s",
        "done",
        "episodes_total",
        "training_iteration",
        "timestamp",
        "timesteps_total",
        "experiment_id",
        "date",
        "timestamp",
        "time_total_s",
        "pid",
        "hostname",
        "node_ip",
        "time_since_restore",
        "timesteps_since_restore",
        "iterations_since_restore",
        "experiment_tag",
        "trial_id",
    }

    # filter attributes into floats, metrics, and config variables
    for key, value in first_trial.items():
        if isinstance(value, float):
            float_keys.append(key)
        if str(key).startswith("config/"):
            config_keys.append(key)
        elif key not in default_names:
            metric_keys.append(key)

    # clean data into a form that front-end client can handle
    for trial, details in trial_details.items():
        ts = os.path.getctime(details["logdir"])
        formatted_time = datetime.datetime.fromtimestamp(ts).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        details["start_time"] = formatted_time
        details["params"] = {}
        details["metrics"] = {}

        # round all floats
        for key in float_keys:
            details[key] = round(details[key], 12)

        # group together config attributes
        for key in config_keys:
            new_name = key[7:]
            details["params"][new_name] = details[key]
            details.pop(key)

        # group together metric attributes
        for key in metric_keys:
            details["metrics"][key] = details[key]
            details.pop(key)

        if details["done"]:
            details["status"] = "TERMINATED"
        else:
            details["status"] = "RUNNING"
        details.pop("done")

        details["job_id"] = os.path.basename(self._logdir)
        details["error"] = "No Error"

    return trial_details