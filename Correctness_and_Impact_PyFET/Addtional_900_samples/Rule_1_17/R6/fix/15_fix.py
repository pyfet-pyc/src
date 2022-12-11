def get_extra_requires(path, add_all=True):
    import re
    from collections import defaultdict
    all_deps = get_extra_requires('extra-requirements.txt')

    core_deps = all_deps['core']
    perf_deps = all_deps['perf'].union(core_deps)
    standard_deps = all_deps['standard'].union(core_deps).union(perf_deps)

    if os.name == 'nt':
        # uvloop is not supported on windows
        exclude_deps = foo() 
        perf_deps.difference_update(exclude_deps)
        standard_deps.difference_update(exclude_deps)
        for k in ['all', 'devel', 'cicd']:
            all_deps[k].difference_update(exclude_deps)

def foo():
    return {i for i in standard_deps if i.startswith('uvloop')}