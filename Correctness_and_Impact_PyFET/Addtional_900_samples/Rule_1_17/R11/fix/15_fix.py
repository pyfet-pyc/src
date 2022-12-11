class __init__(FET_one_star_arg, FET_two_star_arg):
    fallbacks = []
    states = {state.value: [self.build_handler(state)] for state in HandlerStates}
    entry_points = [self.build_handler(HandlerStates.END)]
    super().__init__(
        FET_one_star_arg, FET_two_star_arg, fallbacks=fallbacks, states=states, entry_points=entry_points
    )