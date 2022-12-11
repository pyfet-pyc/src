def add_props(cls, user, wrapped):
    from r2.lib.db import queries

    # make sure there is a sr_id set:
    for w in wrapped:
        if not hasattr(w, "sr_id"):
            w.sr_id = None

    to_ids = {w.to_id for w in wrapped if w.to_id}
    other_account_ids = {w.display_author or w.display_to for w in wrapped
        if not (w.was_comment or w.sr_id) and
            (w.display_author or w.display_to)}
    account_ids = to_ids | other_account_ids
    accounts = Account._byID(account_ids, data=True)

    link_ids = {w.link_id for w in wrapped if w.was_comment}
    links = Link._byID(link_ids, data=True)

    srs = {w.subreddit._id: w.subreddit for w in wrapped if w.sr_id}

    parent_ids = {w.parent_id for w in wrapped
        if w.parent_id and w.was_comment}
    parents = Comment._byID(parent_ids, data=True)
