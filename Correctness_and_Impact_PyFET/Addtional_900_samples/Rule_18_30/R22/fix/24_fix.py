def generate_editable_metadata(
    build_env: BuildEnvironment, backend: Pep517HookCaller, details: str
) -> str:
    """Generate metadata using mechanisms described in PEP 660.

    Returns the generated metadata directory.
    """
    metadata_tmpdir = TempDirectory(kind="modern-metadata", globally_managed=True)

    metadata_dir = metadata_tmpdir.path

    with build_env:
        # Note that Pep517HookCaller implements a fallback for
        # prepare_metadata_for_build_wheel/editable, so we don't have to
        # consider the possibility that this hook doesn't exist.
        runner = runner_with_spinner_message(
            "Preparing editable metadata (pyproject.toml)"
        )
        with backend.subprocess_runner(runner):
            try:
                distinfo_dir = backend.prepare_metadata_for_build_editable(metadata_dir)
            except InstallationSubprocessError as error:
                raise MetadataGenerationFailed(package_details=details) from error

    return os.path.join(metadata_dir, distinfo_dir)
