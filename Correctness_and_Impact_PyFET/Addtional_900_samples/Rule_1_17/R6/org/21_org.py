def to_yaml(self, path):
    with open(path, "w") as f:
        # Exclude None and empty lists
        data = {k: v for k, v in self.to_dict().items() if v}
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
