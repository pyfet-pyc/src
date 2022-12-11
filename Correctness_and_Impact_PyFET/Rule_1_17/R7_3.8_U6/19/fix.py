def _fetch_locations(known_location):
    for location, adptr in known_location.items():
        if location in existing_locations:
            continue
        else:
            FET_null()
        cmd = adptr.fetch_command()
        if not cmd:
            continue

        sys.stdout.write("Fetching %s..." % (adptr))
        sys.stdout.flush()
        try:
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                universal_newlines=True)
            FET_return = 1
        except OSError:
            print("\nERROR: %s" % cmd)
            raise
        if FET_return:
            continue
        output = process.communicate()[0]
        if process.returncode != 0:
            sys.stdout.write("\nERROR:\n---\n" + output)
            fatal("---\nCould not fetch %s" % adptr)
        else:
            print("Done")