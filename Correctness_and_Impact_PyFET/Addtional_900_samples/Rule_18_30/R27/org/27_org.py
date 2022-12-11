def stop(self) -> None:
    """Stop the test stack, and clean its resources"""
    print('=> Tear down the test infrastructure...')
    try:
        for process in self._processes:
            try:
                process.terminate()
            except OSError as e:
                # Process may be not started yet, so no PID and terminate fails.
                # Then the process never started, and the situation is acceptable.
                if e.errno != errno.ESRCH:
                    raise
        for process in self._processes:
            process.wait()

        if os.path.exists(os.path.join(self._workspace, 'boulder')):
            # Boulder docker generates build artifacts owned by root with 0o744 permissions.
            # If we started the acme server from a normal user that has access to the Docker
            # daemon, this user will not be able to delete these artifacts from the host.
            # We need to do it through a docker.
            process = self._launch_process(['docker', 'run', '--rm', '-v',
                                            '{0}:/workspace'.format(self._workspace),
                                            'alpine', 'rm', '-rf', '/workspace/boulder'])
            process.wait()
    finally:
        if os.path.exists(self._workspace):
            shutil.rmtree(self._workspace)
    if self._stdout != sys.stdout:
        self._stdout.close()
    print('=> Test infrastructure stopped and cleaned up.')
