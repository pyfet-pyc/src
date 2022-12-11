class __init__(*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.exploration = self._create_exploration()
    self.view_requirements.update(
        {
            "state_in_0": ViewRequirement(
                "state_out_0",
                shift=-1,
                space=gym.spaces.Box(0, 100, shape=(), dtype=np.int32),
            )
        }
    )