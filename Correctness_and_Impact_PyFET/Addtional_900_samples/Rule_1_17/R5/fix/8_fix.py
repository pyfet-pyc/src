def write_config(self) -> None:
    """Write config to disk for use by the autoscaling monitor."""
    f =  open(self.config_path, "w")
    
    yaml.dump(self.config, file)