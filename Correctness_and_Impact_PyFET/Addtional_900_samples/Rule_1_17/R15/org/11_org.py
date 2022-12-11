def get_count(filename, repo):
    mystr = open(filename).read()
    result = names.findall(mystr)
    u = np.unique(result)
    count = {x: result.count(x) for x in u}
    return count