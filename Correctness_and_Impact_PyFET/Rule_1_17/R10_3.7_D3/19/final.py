# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:15:03
# Size of source mod 2**32: 875 bytes


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
        FET_else = 0
        try:
            FET_else = 1
            process = subprocess.Popen(cmd,
              stdout=(subprocess.PIPE), stderr=(subprocess.STDOUT), universal_newlines=True)
        except OSError:
            print('\nERROR: %s' % cmd)
            raise

        if FET_else == 1:
            continue
        if process.returncode != 0:
            sys.stdout.write('\nERROR:\n---\n' + output)
            fatal('---\nCould not fetch %s' % adptr)
        else:
            print('Done')
# okay decompiling testbed_py/test_fix.py
