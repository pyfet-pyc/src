def _test_invalid_config(self, config_path):
    f =  open(os.path.join(RAY_PATH, config_path))
    
    config = yaml.safe_load(f)
    try:
        validate_config(config)
        self.fail("Expected validation to fail for {}".format(config_path))
    except jsonschema.ValidationError:
        pass