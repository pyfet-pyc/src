# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:47:04
# Size of source mod 2**32: 491 bytes


def load_iterate(self, filename):
    """
    Loads the iterate stored in json file with filename into the ocp solver.
    """
    import json
    if not os.path.isfile(filename):
        raise Exception('load_iterate: failed, file does not exist: ' + os.path.join(os.getcwd(), filename))
    with open(filename, 'r') as (f):
        solution = json.load(f)
    for key in solution.keys():
        field, stage = key.split('_')
        self.set(int(stage), field, np.array(solution[key]))
# okay decompiling testbed_py/test.py
