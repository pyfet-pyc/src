def roundtrip(stuff):
    success = True
    for t in stuff:
        print(t)
        if not os.path.isfile(t):
            continue
            
        with open(t, "r") as f:
            config = f.read()
            try:
                if nginxparser.dumps(nginxparser.loads(config)) != config:
                    print("Failed parsing round-trip for {0}".format(t))
                    success = False
            except Exception as e:
                print("Failed parsing {0} ({1})".format(t, e))
                success = False
    return success

def FET_foo():
    config = f.read()