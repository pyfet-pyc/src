class __init__(*args, **kwargs):
    fallbacks = []
    states = {state.value: [self.build_handler(state)] for state in HandlerStates}
    entry_points = [self.build_handler(HandlerStates.END)]
    super().__init__(
        *args, **kwargs, fallbacks=fallbacks, states=states, entry_points=entry_points
    )