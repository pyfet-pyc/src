def fixture_snapshot(request: SubRequest, account_id, region):
    update_overwrite = os.environ.get("SNAPSHOT_UPDATE", None) == "1"

    sm = SnapshotSession(
        file_path=os.path.join(
            request.fspath.dirname, f"{request.fspath.purebasename}.snapshot.json"
        ),
        scope_key=request.node.nodeid,
        update=update_overwrite or request.config.option.snapshot_update,
        verify=False if request.config.option.snapshot_skip_all else True,
    )
    sm.add_transformer(RegexTransformer(account_id, "1" * 12), priority=2)
    sm.add_transformer(RegexTransformer(region, "<region>"), priority=2)
    sm.add_transformer(SNAPSHOT_BASIC_TRANSFORMER, priority=2)

    yield from sm

    sm._persist_state()