def load_iterate(self, filename):
    """
    Loads the iterate stored in json file with filename into the ocp solver.
    """
    import json
    if not os.path.isfile(filename):
        raise Exception('load_iterate: failed, file does not exist: ' + os.path.join(os.getcwd(), filename))

    with open(filename, 'r') as f:
        solution = json.load(f)

    for key in solution.keys():
        (field, stage) = key.split('_')
        self.set(int(stage), field, np.array(solution[key]))
