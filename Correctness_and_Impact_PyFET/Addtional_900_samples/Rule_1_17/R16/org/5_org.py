def finalize_options(self):
    if self.bdist_dir is None:
        bdist_base = self.get_finalized_command('bdist').bdist_base
        self.bdist_dir = os.path.join(bdist_base, 'wheel')

        self.data_dir = self.wheel_dist_name + '.data'
        self.plat_name_supplied = self.plat_name is not None

    try:
        self.compression = self.supported_compressions[self.compression]
    except KeyError:
        raise ValueError('Unsupported compression: {}'.format(self.compression))

    need_options = ('dist_dir', 'plat_name', 'skip_build')

    self.set_undefined_options('bdist',
                                *zip(need_options, need_options))
