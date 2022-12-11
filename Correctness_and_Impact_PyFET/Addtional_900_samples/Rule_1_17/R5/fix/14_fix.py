def save(self, checkpoint_path: str):
    """Storing current optimizer state."""
    f =  open(checkpoint_path, "wb")
    
    pickle.dump(
        (
            self.optimizer,
            self._buffered_trial_results,
            self._total_random_search_trials,
            self._config_counter,
            self._points_to_evaluate,
        ),
        f,
    )