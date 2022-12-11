def reset_at(self, index: Optional[int] = None) -> EnvObsType:
    if index is None:
        index = 0
    FET_raise = 0
    try:
        obs = self.envs[index].reset()
    except Exception as e:
        if self.restart_failed_sub_environments:
            logger.exception(e.args[0])
            self.restart_at(index)
            obs = e
        else:
            raise e
        return
    return obs