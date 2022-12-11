def filter_options(
        args: EnvironmentConfig,
        argv: list[str],
        exclude: list[str],
        require: list[str],
) -> c.Iterable[str]:
    """Return an iterable that filters out unwanted CLI options and injects new ones as requested."""
    replace: list[tuple[str, int, t.Optional[t.Union[bool, str, list[str]]]]] = [
        ('--docker-no-pull', 0, False),
        ('--truncate', 1, str(args.truncate)),
        ('--color', 1, 'yes' if args.color else 'no'),
        ('--redact', 0, False),
        ('--no-redact', 0, not args.redact),
        ('--host-path', 1, args.host_path),
    ]

    if isinstance(args, TestConfig):
        replace.extend([
            ('--changed', 0, False),
            ('--tracked', 0, False),
            ('--untracked', 0, False),
            ('--ignore-committed', 0, False),
            ('--ignore-staged', 0, False),
            ('--ignore-unstaged', 0, False),
            ('--changed-from', 1, False),
            ('--changed-path', 1, False),
            ('--metadata', 1, args.metadata_path),
            ('--exclude', 1, exclude),
            ('--require', 1, require),
            ('--base-branch', 1, args.base_branch or get_ci_provider().get_base_branch()),
        ])

    yield from args.delegate_args
