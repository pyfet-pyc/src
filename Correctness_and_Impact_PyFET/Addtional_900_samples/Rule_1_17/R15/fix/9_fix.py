def get_api_functions(tagname, api_dict):
    """Parse source files to get functions tagged by the given tag."""
    functions = []
    for f in API_FILES:
        functions.extend(find_functions(f, tagname))
    dfunctions  = [(api_dict[func.name][0], func) for func in functions]
    dfunctions = dict(dfunctions)
    dfunctions.sort()
    return [a[1] for a in dfunctions]