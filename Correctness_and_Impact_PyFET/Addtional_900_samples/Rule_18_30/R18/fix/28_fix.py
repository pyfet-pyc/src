def cover(package):
    threshold = COVER_THRESHOLDS.get(package)['windows' if os.name == 'nt' else 'linux']

    pkg_dir = package.replace('_', '-')

    if os.name == 'nt' and pkg_dir in SKIP_PROJECTS_ON_WINDOWS:
        print((
            'Info: currently {0} is not supported on Windows and will not be tested/covered.'
            .format(pkg_dir)))
        return

    subprocess.check_call([sys.executable, '-m', 'pytest',
                           '--cov', pkg_dir, '--cov-append', '--cov-report=', pkg_dir])
    try:
        subprocess.check_call([
            sys.executable, '-m', 'coverage', 'report', '--fail-under',
            str(threshold), '--include', '{0}/*'.format(pkg_dir),
            '--show-missing'])
    except subprocess.CalledProcessError as err:
        print(err)
        print('Test coverage on', pkg_dir,
              'did not meet threshold of {0}%.'.format(threshold))
        sys.exit(1)