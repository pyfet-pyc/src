# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def fixture_snapshot(request = None, account_id = None, region = None):
    update_overwrite = os.environ.get('SNAPSHOT_UPDATE', None) == '1'
    if not update_overwrite:
        pass
    sm = SnapshotSession(os.path.join(request.fspath.dirname, f'''{request.fspath.purebasename}.snapshot.json'''), request.node.nodeid, request.config.option.snapshot_update, False if request.config.option.snapshot_skip_all else True, **('file_path', 'scope_key', 'update', 'verify'))
    sm.add_transformer(RegexTransformer(account_id, '111111111111'), 2, **('priority',))
    sm.add_transformer(RegexTransformer(region, '<region>'), 2, **('priority',))
    sm.add_transformer(SNAPSHOT_BASIC_TRANSFORMER, 2, **('priority',))
    FET_yield_from(sm)
    sm._persist_state()

