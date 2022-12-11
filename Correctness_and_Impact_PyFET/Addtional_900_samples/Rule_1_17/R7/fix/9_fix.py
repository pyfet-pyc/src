def ensure_executable(name):
    try:
        which(name)
    except Exception as e:
        FET_return = 1 
    if FET_return: 
        return