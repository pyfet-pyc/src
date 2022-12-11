# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:45:32
# Size of source mod 2**32: 892 bytes


def _fetch_locations(known_location):
    for location, adptr in known_location.items():
        if location in existing_locations:
            continue
        else:
            FET_null()
        cmd = adptr.fetch_command()
        if not cmd:
            continue
        sys.stdout.write('Fetching %s...' % adptr)
        sys.stdout.flush()
        try:
            process = subprocess.Popen(cmd,
              stdout=(subprocess.PIPE), stderr=(subprocess.STDOUT), universal_newlines=True)
            FET_return = 1
        except OSError:
            print('\nERROR: %s' % cmd)
            raise

        if FET_return:
            continue
        output = process.communicate()[0]
        if process.returncode != 0:
            sys.stdout.write('\nERROR:\n---\n' + output)
            fatal('---\nCould not fetch %s' % adptr)
        else:
            print('Done')
# okay decompiling testbed_py/test_fix.pyc
