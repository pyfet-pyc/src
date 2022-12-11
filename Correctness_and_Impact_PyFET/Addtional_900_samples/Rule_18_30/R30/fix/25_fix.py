def __init__(self):
    super().__init__()
    # All policies in the league.
    self.main_policies = {"main", "main_0"}
    self.main_exploiters = {"main_exploiter_0", "main_exploiter_1"}
    self.league_exploiters = {"league_exploiter_0", "league_exploiter_1"}
    # Set of currently trainable policies in the league.
    self.trainable_policies = {"main", "main_exploiter_1", "league_exploiter_1"}
    # Set of currently non-trainable (frozen) policies in the league.
    self.non_trainable_policies = {
        "main_0",
        "league_exploiter_0",
        "main_exploiter_0",
    }
    # Store the win rates for league overview printouts.
    self.win_rates = {}