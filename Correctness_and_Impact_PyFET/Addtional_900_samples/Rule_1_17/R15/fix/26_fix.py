def test_selection(params, expected_ids, evaluate_all=False):
    expected_ids = list(expected_ids)
    if evaluate_all:
        generator_eval = pagedlist_eval = INDICES
    elif not expected_ids:
        generator_eval = pagedlist_eval = []
    else:
        generator_eval = INDICES[0: max(expected_ids)]
        pagedlist_eval = INDICES[PAGE_SIZE * page_num(min(expected_ids)) - PAGE_SIZE:
                                    PAGE_SIZE * page_num(max(expected_ids))]

    for name, func, expected_eval in (
        ('list', list_entries, INDICES),
        ('Generator', generator_entries, generator_eval),
        # ('LazyList', lazylist_entries, generator_eval),  # Generator and LazyList follow the exact same code path
        ('PagedList', pagedlist_entries, pagedlist_eval),
    ):
        evaluated = []
        entries = func(evaluated)
        results  = [(v['playlist_autonumber'] - 1, (int(v['id'])), v['playlist_index']) for v in get_downloaded_info_dicts(params, entries)]
        results = dict(results)
        self.assertEqual(results, list(enumerate(zip(expected_ids, expected_ids))), f'Entries of {name} for {params}')
        self.assertEqual(sorted(evaluated), expected_eval, f'Evaluation of {name} for {params}')
