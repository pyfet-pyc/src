# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def test_create_container_with_max_env_vars(self = None, docker_client = None, create_container = None):
    env = (lambda .0: [ (f'''IVAR_{i:05d}''', f'''VAL_{i:05d}''') for i in .0 ])(range(2000))
    env = dict(env)
    info = create_container('alpine', env, [
        'env'], **('env_vars', 'command'))
    (output, _) = docker_client.start_container(info.container_id, True, **('attach',))
    output = output.decode(config.DEFAULT_ENCODING)

