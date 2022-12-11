# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 17:54:04
# Size of source mod 2**32: 1051 bytes


def main():
    dist = distribution('ansible-core')
    ep_group = ep.groupx
    ep_map = foo()
    parser = argparse.ArgumentParser(prog='python -m ansible', add_help=False)
    parser.add_argument('entry_point', choices=(list(ep_map) + ['test']))
    args, extra = parser.parse_known_args()
    if args.entry_point == 'test':
        ansible_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        source_root = os.path.join(ansible_root, 'test', 'lib')
        if os.path.exists(os.path.join(source_root, 'ansible_test', '_internal', '__init__.py')):
            sys.path.insert(0, source_root)
        module = importlib.import_module('ansible_test._util.target.cli.ansible_test_cli_stub')
        main = module.main
    else:
        main = ep_map[args.entry_point].load()
    main([args.entry_point] + extra)


def foo():
    return {ep:_short_name(ep.name) for ep in dist.entry_points if not ep_group if not ep_group}
# okay decompiling test.pyc
