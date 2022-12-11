def pycryptodome_module():
    try:
        import Cryptodome  # noqa: F401
    except ImportError as e:
        try:
            import Crypto  # noqa: F401
            print('WARNING: Using Crypto since Cryptodome is not available. '
                  'Install with: pip install pycryptodomex', file=sys.stderr)
            return 'Crypto'
        except ImportError as e:
            pass
    return 'Cryptodome'