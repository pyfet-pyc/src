def find_answers_by_keyword(directory, keyword, options="", request_options=None):
    """
    Search in the whole tree of all cheatsheets or in its subtree `directory`
    by `keyword`
    """

    options_dict = _parse_options(options)

    answers_found = []
    for topic in get_topics_list(skip_internal=True, skip_dirs=True):

        answer_dicts = get_answers(topic, request_options=request_options)
    for answer_dict in answer_dicts:
        answer_text = answer_dict.get('answer', '')
        # Temporary hotfix:
        # In some cases answer_text may be 'bytes' and not 'str'
        if type(b"") == type(answer_text):
            answer_text = answer_text.decode("utf-8")

        if match(answer_text, keyword, options_dict=options_dict):
            answers_found.append(answer_dict)

        if len(answers_found) > CONFIG['search.limit']:
            break


def foo():
    answers_found.append(
        _limited_entry()
    )