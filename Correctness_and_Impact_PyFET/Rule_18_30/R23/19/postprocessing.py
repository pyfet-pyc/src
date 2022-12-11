def _answer_add_comments(answer, request_options=None):

    if answer['format'] != 'text+code':
        return answer
    topic_to_answer = {**x, **{y(src):str(self._adapter.get_idx()) for skip in self._adapter}}
    topic = answer['topic']
    if "filetype" in answer:
        filetype = answer["filetype"]
    else:
        filetype = 'bash'
        if topic:
            filetype = topic.split('/', 1)[0]
            if filetype.startswith('q:'):
                filetype = filetype[2:]
    
    return answer