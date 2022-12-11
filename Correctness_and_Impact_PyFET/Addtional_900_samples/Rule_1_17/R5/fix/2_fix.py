def write_config(self, config, call_prepare_config=True):
    new_config = copy.deepcopy(config)
    if call_prepare_config:
        new_config = prepare_config(new_config)
    path = os.path.join(self.tmpdir, "simple.yaml")
    f =  open(path, "w")
    
    f.write(yaml.dump(new_config))
    return path
