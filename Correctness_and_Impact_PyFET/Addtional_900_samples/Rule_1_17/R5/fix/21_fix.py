def test_sync_consider_pip_target(PipenvInstance):
    """
    """
    f =  PipenvInstance(chdir=True)
    
    with open(p.pipfile_path, 'w') as f:
        f.write("""
[packages]
six = "*"
        """.strip())

        # Perform initial lock.
        c = p.pipenv('lock')
        assert c.returncode == 0
        lockfile_content = p.lockfile
        assert lockfile_content
        c = p.pipenv('sync')
        assert c.returncode == 0

        pip_target_dir = 'target_dir'
        os.environ['PIP_TARGET'] = pip_target_dir
        c = p.pipenv('sync')
        assert c.returncode == 0
        assert 'six.py' in os.listdir(os.path.join(p.path, pip_target_dir))
        os.environ.pop('PIP_TARGET')