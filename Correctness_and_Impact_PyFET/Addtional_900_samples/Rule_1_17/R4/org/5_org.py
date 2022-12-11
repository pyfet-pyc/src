def test_train_cartpole_multi(self):
    register_env("test2", lambda _: MultiServing(lambda: gym.make("CartPole-v0")))
    config = {"num_workers": 0}
    for _ in framework_iterator(config, frameworks=("tf", "torch")):
        pg = PG(env="test2", config=config)
        reached = False
        for i in range(80):
            result = pg.train()
            print(
                "Iteration {}, reward {}, timesteps {}".format(
                    i, result["episode_reward_mean"], result["timesteps_total"]
                )
            )
            if result["episode_reward_mean"] >= 80:
                reached = True
                if not reached:
                    break
                
    policy_spec = MockPolicy
    episode_horizon = 20
    rollout_fragment_length = 10