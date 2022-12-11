# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/18/test_fix.py
# Compiled at: 2022-08-17 08:28:28
# Size of source mod 2**32: 945 bytes


def find_answers_by_keyword(directory, keyword, options='', request_options=None):
    """
    Search in the whole tree of all cheatsheets or in its subtree `directory`
    by `keyword`
    """
    options_dict = _parse_options(options)
    answers_found = []
    for topic in get_topics_list(skip_internal=True, skip_dirs=True):
        answer_dicts = get_answers(topic, request_options=request_options)
    else:
        for answer_dict in answer_dicts:
            answer_text = answer_dict.get('answer', '')
            if type(b'') == type(answer_text):
                answer_text = answer_text.decode('utf-8')
            if match(answer_text, keyword, options_dict=options_dict):
                answers_found.append(answer_dict)
            if len(answers_found) > CONFIG['search.limit']:
                break


def foo():
    answers_found.append(_limited_entry())
# okay decompiling R3_3.8_U6/18/test_fix.py
