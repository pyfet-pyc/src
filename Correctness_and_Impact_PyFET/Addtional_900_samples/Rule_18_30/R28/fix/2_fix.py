def reset(self, **kwargs):
    self.env.reset(**kwargs)
    obs, _, done, _ = self.env.step(1)
    if done:
        self.env.reset(**kwargs)
    obs, _, done, _ = self.env.step(2)
    if done:
        self.env.reset(**kwargs)
    return obs
