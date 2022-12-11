def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('targets', nargs='+', choices=['ALL', 'DNS_PLUGINS', 'certbot', *PLUGINS],
                        help='the list of snaps to build')
    parser.add_argument('--archs', nargs='+', choices=['amd64', 'arm64', 'armhf'],
                        default=['amd64'], help='the architectures for which snaps are built')
    parser.add_argument('--timeout', type=int, default=None,
                        help='build process will fail after the provided timeout (in seconds)')
    args = parser.parse_args()

    archs = set(args.archs)
    targets = set(args.targets)

    if 'ALL' in targets:
        targets.remove('ALL')
        targets.update(['certbot', 'DNS_PLUGINS'])

    if 'DNS_PLUGINS' in targets:
        targets.remove('DNS_PLUGINS')
        targets.update(PLUGINS)

    # If we're building anything other than just Certbot, we need to
    # generate the snapcraft files for the DNS plugins.
    if targets != {'certbot'}:
        subprocess.run(['tools/snap/generate_dnsplugins_all.sh'],
                       check=True, cwd=CERTBOT_DIR)

    print('Start remote snap builds...')
    print(f' - archs: {", ".join(archs)}')
    print(f' - projects: {", ".join(sorted(targets))}')
    print()

    manager: SyncManager = Manager()
    pool = Pool(processes=len(targets))
    with manager, pool:
        status: Dict[str, Dict[str, str]] = manager.dict()
        running = manager.dict({target: True for target in targets})
        # While multiple processes are running, this lock should be acquired
        # before printing output.
        output_lock = manager.Lock()

        async_results = [pool.apply_async(_build_snap, (target, archs, status, running, output_lock))
                         for target in targets]

        process = Process(target=_dump_status, args=(archs, status, running, output_lock))
        process.start()

        try:
            process.join(args.timeout)

            if process.is_alive():
                for target in targets:
                    if target == 'certbot':
                        workspace = CERTBOT_DIR
                    else:
                        workspace = join(CERTBOT_DIR, target)
                    _dump_failed_build_logs(target, archs, status, workspace)
                raise ValueError(f"Timeout out reached ({args.timeout} seconds) during the build!")

            build_success = True
            for async_result in async_results:
                if not async_result.get():
                    build_success = False

            _dump_results(archs, status)
            if build_success:
                print('All builds succeeded.')
            else:
                print('Some builds failed.')
                raise ValueError("There were failures during the build!")
        finally:
            process.terminate()
