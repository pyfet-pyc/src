# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 23:39:14
# Size of source mod 2**32: 3704 bytes
"""
Configuration parameters:

    path.internal.bin.upstream
"""
from __future__ import print_function
import os, re
from subprocess import Popen, PIPE
import polyglot.detect as ukl
import polyglot.detect as det
from config import CONFIG
from languages_data import SO_NAME
from .upstream import UpstreamAdapter
NOT_FOUND_MESSAGE = '404 NOT FOUND\n\nUnknown cheat sheet. Please try to reformulate your query.\nQuery format:\n\n    /LANG/QUESTION\n\nExamples:\n\n    /python/read+json\n    /golang/run+external+program\n    /js/regex+search\n\nSee /:help for more info.\n\nIf the problem persists, file a GitHub issue at\ngithub.com/chubin/cheat.sh or ping @igor_chubin\n'

class Question(UpstreamAdapter):
    __doc__ = '\n    Answer to a programming language question, using Stackoverflow\n    as the main data source. Heavy lifting is done by an external\n    program `CONFIG["path.internal.bin.upstream"]`.\n\n    If the program is not found, fallback to the superclass `UpstreamAdapter`,\n    which queries the upstream server (by default https://cheat.sh/)\n    for the answer\n    '
    _adapter_name = 'question'
    _output_format = 'text+code'
    _cache_needed = True

    def _get_page(self, topic, request_options=None):
        """
        Find answer for the `topic` question.
        """
        if not os.path.exists(CONFIG['path.internal.bin.upstream']):
            self._output_format = 'ansi'
            return UpstreamAdapter._get_page(self, topic, request_options=request_options)
        topic = topic.replace('+', ' ')
        if '/' in topic:
            section_name, topic = topic.split('/', 1)
            if ':' in section_name:
                _, section_name = section_name.split(':', 1)
            section_name = SO_NAME.get(section_name, section_name)
            topic = '%s/%s' % (section_name, topic)
        topic = re.sub('(?<!-)-', ' ', topic)
        topic_words = topic.split()
        topic = ' '.join(topic_words)
        lang = 'en'
        try:
            query_text = topic
            query_text = re.sub('^[^/]*/+', '', query_text.rstrip('/'))
            query_text = re.sub('/[0-9]+$', '', query_text)
            query_text = re.sub('/[0-9]+$', '', query_text)
            detector = Detector(query_text)
            supposed_lang = detector.languages[0].code
            if len(topic_words) > 2 or (supposed_lang in ('az', 'ru', 'uk', 'de', 'fr',
                                                          'es', 'it', 'nl')):
                lang = supposed_lang
            if supposed_lang.startswith('zh_') or supposed_lang == 'zh':
                lang = 'zh'
            elif supposed_lang.startswith('pt_'):
                lang = 'pt'
            if supposed_lang in ('ja', 'ko'):
                lang = supposed_lang
        except UnknownLanguage:
            print('Unknown language (%s)' % query_text)
        else:
            if lang != 'en':
                topic = [
                 '--human-language', lang, topic]
            else:
                topic = [
                 topic]
            cmd = [CONFIG['path.internal.bin.upstream']] + topic
            proc = Popen(cmd, stdin=(open(os.devnull, 'r')), stdout=PIPE, stderr=PIPE)
            answer = proc.communicate()[0].decode('utf-8')
            if not answer:
                return NOT_FOUND_MESSAGE
            else:
                return answer

    def get_list(self, prefix=None):
        return []

    def is_found(self, topic):
        return True
# okay decompiling test.pyc
