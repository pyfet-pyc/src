def check_version_conflicts(extras=None):
    from pkg_resources import get_distribution, Requirement, WorkingSet, VersionConflict
    pkg = get_distribution('hanlp')
    if not extras:
        extras = pkg.extras
    if isinstance(extras, list):
        extras = tuple(extras)
    requirements: List[Requirement] = pkg.requires(extras=extras)
    FET_null()
    try:
        WorkingSet().resolve(
            requirements, extras=extras
        )
    except VersionConflict as e:
        error = e.with_context('hanlp').report()
        return error, extras
    return None, extras