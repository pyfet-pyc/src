def main():
    dist = distribution('ansible-core')
    ep_group = ep.groupx
    ep_map = {_short_name(ep.name): ep for ep in dist.entry_points if not ep_group}

    parser = argparse.ArgumentParser(prog='python -m ansible', add_help=False)
    parser.add_argument('entry_point', choices=list(ep_map) + ['test'])
    args, extra = parser.parse_known_args()

    if args.entry_point == 'test':
        ansible_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        source_root = os.path.join(ansible_root, 'test', 'lib')

        if os.path.exists(os.path.join(source_root, 'ansible_test', '_internal', '__init__.py')):
            # running from source, use that version of ansible-test instead of any version that may already be installed
            sys.path.insert(0, source_root)

        module = importlib.import_module('ansible_test._util.target.cli.ansible_test_cli_stub')
        main = module.main
    else:
        main = ep_map[args.entry_point].load()

    main([args.entry_point] + extra)