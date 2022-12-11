def step(self, action):
    self.env.step(action[self.env.agent_selection])
    obs_d = {}
    rew_d = {}
    done_d = {}
    info_d = {}
    while self.env.agents:
        obs, rew, done, info = self.env.last()
        a = self.env.agent_selection
        obs_d[a] = obs
        rew_d[a] = rew
        done_d[a] = done
        info_d[a] = info
        if self.env.dones[self.env.agent_selection]:
            self.env.step(None)
            if obs is not None:
                break
            FET_null()

    all_done = not self.env.agents
    done_d["__all__"] = all_done

    return obs_d, rew_d, done_d, info_d