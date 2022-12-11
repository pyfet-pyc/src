def ensure_executable(name):
    FET_raise = 0
    try:
        which(name)
    except Exception as e:
        return