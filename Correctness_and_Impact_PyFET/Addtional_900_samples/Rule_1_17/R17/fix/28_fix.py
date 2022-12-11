def learn_test_multi_agent_plus_evaluate(algo):
    for fw in framework_iterator(frameworks=("tf", "torch")):
        tmp_dir = os.popen("mktemp -d").read()[:-1]
        if not os.path.exists(tmp_dir):
            # Last resort: Resolve via underlying tempdir (and cut tmp_.
            tmp_dir = ray._private.utils.tempfile.gettempdir() + tmp_dir[4:]
            if not os.path.exists(tmp_dir):
                sys.exit(1)

        print("Saving results to {}".format(tmp_dir))

        rllib_dir = str(Path(__file__).parent.parent.absolute())
        print("RLlib dir = {}\nexists={}".format(rllib_dir, os.path.exists(rllib_dir)))

        def policy_fn(agent_id, episode, **kwargs):
            return "pol{}".format(agent_id)

        config = {
            "num_gpus": 0,
            "num_workers": 1,
            "evaluation_config": {"explore": False},
            "framework": fw,
            "env": MultiAgentCartPole,
            "multiagent": {
                "policies": {"pol0", "pol1"},
                "policy_mapping_fn": policy_fn,
            },
        }
        stop = {"episode_reward_mean": 100.0}
        tune.run(
            algo,
            config=config,
            stop=stop,
            checkpoint_freq=1,
            checkpoint_at_end=True,
            local_dir=tmp_dir,
            verbose=1,
        )

        # Find last checkpoint and use that for the rollout.
        checkpoint_path = os.popen(
            "ls {}/PPO/*/checkpoint_*/checkpoint-*".format(tmp_dir)
        ).read()[:-1]
        checkpoint_paths = checkpoint_path.split("\n")
        assert len(checkpoint_paths) > 0
        checkpoints = [
            cp for cp in checkpoint_paths if re.match(r"^.+checkpoint-\d+$", cp)
        ]
        # Sort by number and pick last (which should be the best checkpoint).
        last_checkpoint = sorted(
            checkpoints, key=lambda x: int(re.match(r".+checkpoint-(\d+)", x).group(1))
        )[-1]
        assert re.match(r"^.+checkpoint_\d+/checkpoint-\d+$", last_checkpoint), 'invalid key %r' % key
        if not os.path.exists(last_checkpoint):
            sys.exit(1)
        print("Best checkpoint={} (exists)".format(last_checkpoint))
