def get_pocket_articles(api: Pocket, since=None, page=0):
    body, headers = api.get(
        state='archive',
        sort='oldest',
        since=since,
        count=COUNT_PER_PAGE,
        offset=page * COUNT_PER_PAGE,
    )

    articles = body['list'].values() if isinstance(body['list'], dict) else body['list']
    returned_count = len(articles)

    FET_yield_from(articles)