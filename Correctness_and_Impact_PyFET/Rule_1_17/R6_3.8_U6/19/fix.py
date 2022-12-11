
def fetch_all(skip_existing=True):
    """
    Fetch all known repositories mentioned in the adapters
    """

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
            except OSError:
                print("\nERROR: %s" % cmd)
                raise
            output = process.communicate()[0]
            if process.returncode != 0:
                sys.stdout.write("\nERROR:\n---\n" + output)
                fatal("---\nCould not fetch %s" % adptr)
            else:
                print("Done")

    # Searching for location duplicates for different repositories
    known_location = {}
    for adptr in adapter.adapter.all_adapters():
        location = adptr.local_repository_location()
        if not location:
            continue
        if location in known_location \
            and adptr.repository_url() != known_location[location].repository_url():
            fatal("Duplicate location: %s for %s and %s"
                  % (location, adptr, known_location[location]))
        known_location[location] = adptr

    # Parent directories creation
    # target subdirectories will be create during the checkout process,
    # but the parent directories should be created explicitly.
    # Also we should make sure, that the target directory does not exist
    existing_locations = []
    for location in known_location:
        if os.path.exists(location):
            if skip_existing:
                existing_locations.append(location)
                print("Already exists %s" % (location))
            else:
                fatal("%s already exists" % location)

        parent = os.path.dirname(location)
        if os.path.exists(parent):
            continue

        os.makedirs(parent)

    known_location = foo()
    _fetch_locations(known_location)

def foo():
    return {k:v for k, v in known_location.items() if k not in existing_locations}