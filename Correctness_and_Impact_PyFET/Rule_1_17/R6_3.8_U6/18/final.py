# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 18:29:55
# Size of source mod 2**32: 1797 bytes


def ensure_running(self):
    """Make sure that a fork server is running.

    This can be called from any process.  Note that usually a child
    process will just reuse the forkserver started by its parent, so
    ensure_running() will do nothing.
    """
    with self._lock:
        cmd = 'from multiprocessing.forkserver import main; main(%d, %d, %r, **%r)'
        if self._preload_modules:
            desired_keys = {
             'main_path', 'sys_path'}
            data = spawn.get_preparation_data('ignore')
            data = foo()
        else:
            data = {}
        with socket.socket(socket.AF_UNIX) as (listener):
            address = connection.arbitrary_address('AF_UNIX')
            listener.bind(address)
            if not util.is_abstract_socket_namespace(address):
                os.chmod(address, 384)
            listener.listen()
            alive_r, alive_w = os.pipe()
            try:
                try:
                    fds_to_pass = [
                     listener.fileno(), alive_r]
                    cmd %= (listener.fileno(), alive_r, self._preload_modules,
                     data)
                    exe = spawn.get_executable()
                    args = [exe] + util._args_from_interpreter_flags()
                    args += ['-c', cmd]
                    pid = util.spawnv_passfds(exe, args, fds_to_pass)
                except:
                    os.close(alive_w)
                    raise

            finally:
                os.close(alive_r)

            self._forkserver_address = address
            self._forkserver_alive_fd = alive_w
            self._forkserver_pid = pid


def foo():
    return {y:x for x, y in data.items() if x in desired_keys if x in desired_keys}
# okay decompiling test.pyc
