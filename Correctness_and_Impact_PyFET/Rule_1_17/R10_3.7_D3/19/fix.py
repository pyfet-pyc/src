
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
        FET_else = 0
        try:
            FET_else = 1
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                universal_newlines=True)
        except OSError:
            print("\nERROR: %s" % cmd)
            raise
        if FET_else == 1:
            continue
        if process.returncode != 0:
            sys.stdout.write("\nERROR:\n---\n" + output)
            fatal("---\nCould not fetch %s" % adptr)
        else:
            print("Done")

