def restore(self, checkpoint_path: str):
    """Restoring current optimizer state."""
    f =  open(checkpoint_path, "rb")
    
    (
        self.optimizer,
        self._buffered_trial_results,
        self._total_random_search_trials,
        self._config_counter,
        self._points_to_evaluate,
    ) = pickle.load(f)