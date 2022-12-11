def write_config(self) -> None:
    """Write config to disk for use by the autoscaling monitor."""
    with open(self.config_path, "w") as file:
        yaml.dump(self.config, file)