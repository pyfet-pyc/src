def test_update_live_symlinks(self):
    """Test update_live_symlinks"""
    # create files with incorrect symlinks
    from certbot._internal import cert_manager
    archive_paths = {}
    for domain in self.domains:
        custom_archive = self.domains[domain]
        if custom_archive is not None:
            archive_dir_path = custom_archive
        else:
            archive_dir_path = os.path.join(self.config.default_archive_dir, domain)
        archive_paths[domain] = {kind:
            os.path.join(archive_dir_path, kind + "1.pem") for kind in ALL_FOUR}
        for kind in ALL_FOUR:
            live_path = self.config_files[domain][kind]
            archive_path = archive_paths[domain][kind]
            open(archive_path, 'a').close()
            # path is incorrect but base must be correct
            os.symlink(os.path.join(self.config.config_dir, kind + "1.pem"), live_path)

    # run update symlinks
    cert_manager.update_live_symlinks(self.config)

    # check that symlinks go where they should
    prev_dir = os.getcwd()
    try:
        for domain in self.domains:
            for kind in ALL_FOUR:
                os.chdir(os.path.dirname(self.config_files[domain][kind]))
                self.assertEqual(
                    filesystem.realpath(filesystem.readlink(self.config_files[domain][kind])),
                    filesystem.realpath(archive_paths[domain][kind]))
    finally:
        os.chdir(prev_dir)
