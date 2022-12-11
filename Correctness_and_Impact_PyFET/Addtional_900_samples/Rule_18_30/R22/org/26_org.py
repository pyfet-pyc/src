def install(
    install_options: List[str],
    global_options: Sequence[str],
    root: Optional[str],
    home: Optional[str],
    prefix: Optional[str],
    use_user_site: bool,
    pycompile: bool,
    scheme: Scheme,
    setup_py_path: str,
    isolated: bool,
    req_name: str,
    build_env: BuildEnvironment,
    unpacked_source_directory: str,
    req_description: str,
) -> bool:

    header_dir = scheme.headers

    with TempDirectory(kind="record") as temp_dir:
        try:
            record_filename = os.path.join(temp_dir.path, "install-record.txt")
            install_args = make_setuptools_install_args(
                setup_py_path,
                global_options=global_options,
                install_options=install_options,
                record_filename=record_filename,
                root=root,
                prefix=prefix,
                header_dir=header_dir,
                home=home,
                use_user_site=use_user_site,
                no_user_config=isolated,
                pycompile=pycompile,
            )

            runner = runner_with_spinner_message(
                f"Running setup.py install for {req_name}"
            )
            with build_env:
                runner(
                    cmd=install_args,
                    cwd=unpacked_source_directory,
                )

            if not os.path.exists(record_filename):
                logger.debug("Record file %s not found", record_filename)
                # Signal to the caller that we didn't install the new package
                return False

        except Exception as e:
            # Signal to the caller that we didn't install the new package
            raise LegacyInstallFailure(package_details=req_name) from e

        # At this point, we have successfully installed the requirement.

        # We intentionally do not use any encoding to read the file because
        # setuptools writes the file using distutils.file_util.write_file,
        # which does not specify an encoding.
        with open(record_filename) as f:
            record_lines = f.read().splitlines()

    write_installed_files_from_setuptools_record(record_lines, root, req_description)
    return True
