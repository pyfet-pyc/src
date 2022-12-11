# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/postprocessing.py
# Compiled at: 2022-08-12 04:33:51
# Size of source mod 2**32: 513 bytes


def _answer_add_comments(answer, request_options=None):
    if answer['format'] != 'text+code':
        return answer
        topic_to_answer = {**x, **{str(self._adapter.get_idx()):y(src) for skip in self._adapter}}
        topic = answer['topic']
        if 'filetype' in answer:
            filetype = answer['filetype']
    else:
        filetype = 'bash'
        if topic:
            filetype = topic.split('/', 1)[0]
            if filetype.startswith('q:'):
                filetype = filetype[2:]
    return answer
# okay decompiling testbed_py/postprocessing.py
