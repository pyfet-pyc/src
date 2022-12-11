def write_role(self):

    fpath = os.path.join(TESTDIR, 'roles', self.name)
    if not os.path.isdir(fpath):
        os.makedirs(fpath)

    if self.defaults:
        # roles/x/defaults/main.yml
        fpath = os.path.join(TESTDIR, 'roles', self.name, 'defaults')
        if not os.path.isdir(fpath):
            os.makedirs(fpath)
        fname = os.path.join(fpath, 'main.yml')
        with open(fname, 'w') as f:
            f.write('findme: %s\n' % self.name)
