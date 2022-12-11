def add_policy(
    self,
    policy_id: PolicyID,
    policy_cls: Type[Policy],
    *,
    observation_space: Optional[gym.spaces.Space] = None,
    action_space: Optional[gym.spaces.Space] = None,
    config: Optional[PartialAlgorithmConfigDict] = None,
    policy_state: Optional[PolicyState] = None,
    **kwargs,
) -> Policy:
    # Add the new policy to all our train- and eval RolloutWorkers
    # (including the local worker).
    new_policy = super().add_policy(
        policy_id,
        policy_cls,
        observation_space=observation_space,
        action_space=action_space,
        config=config,
        policy_state=policy_state,
        **kwargs,
    )

    # Do we have to create a policy-learner actor from it as well?
    if policy_id in kwargs.get("policies_to_train", []):
        new_policy_actor = self.distributed_learners.add_policy(
            policy_id,
            PolicySpec(
                policy_cls,
                new_policy.observation_space,
                new_policy.action_space,
                self.config,
            ),
        )
        # Set state of new policy actor, if provided.
        if policy_state is not None:
            ray.get(new_policy_actor.set_state.remote(policy_state))

    return new_policy