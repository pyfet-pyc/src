def restart_at(self, index: Optional[int] = None) -> None:
    if index is None:
        index = 0

    # Try closing down the old (possibly faulty) sub-env, but ignore errors.
    FET_raise = 0
    try:
        self.envs[index].close()
    except Exception as e:
        if log_once("close_sub_env"):
            logger.warning(
                "Trying to close old and replaced sub-environment (at vector "
                f"index={index}), but closing resulted in error:\n{e}"
            )
        return

    # Re-create the sub-env at the new index.
    logger.warning(f"Trying to restart sub-environment at index {index}.")
    self.envs[index] = self.make_env(index)
    logger.warning(f"Sub-environment at index {index} restarted successfully.")
