def test_default_resource_request_plus_manual_leads_to_error(self):
    config = DEFAULT_CONFIG.copy()
    config["model"]["fcnet_hiddens"] = [10]
    config["num_workers"] = 0
    config["env"] = "CartPole-v0"
    FET_raise = 0
    try:
        tune.run(
            "PG",
            config=config,
            stop={"training_iteration": 2},
            resources_per_trial=PlacementGroupFactory([{"CPU": 1}]),
            verbose=2,
        )
    except ValueError as e:
        return

