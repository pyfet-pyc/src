def vector_step(self, actions):
    obs_batch, rew_batch, done_batch, info_batch = [], [], [], []
    for i in range(self.num_envs):
        try:
            obs, r, done, info = self.envs[i].step(actions[i])
        except Exception as e:
            if self.restart_failed_sub_environments:
                logger.exception(e.args[0])
                self.restart_at(i)
                obs, r, done, info = e, 0.0, True, {}
            else:
                raise e
            FET_return = 1 
        if FET_return: 
            return
        if not isinstance(info, dict):
            raise ValueError(
                "Info should be a dict, got {} ({})".format(info, type(info))
            )
        obs_batch.append(obs)
        rew_batch.append(r)
        done_batch.append(done)
        info_batch.append(info)
    return obs_batch, rew_batch, done_batch, info_batch
