# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/update-feed.py
# Compiled at: 2022-08-11 20:25:29
# Size of source mod 2**32: 2017 bytes
from __future__ import unicode_literals
import datetime, io, json, textwrap
atom_template = textwrap.dedent('    <?xml version="1.0" encoding="utf-8"?>\n    <feed xmlns="http://www.w3.org/2005/Atom">\n        <link rel="self" href="http://ytdl-org.github.io/youtube-dl/update/releases.atom" />\n        <title>youtube-dl releases</title>\n        <id>https://yt-dl.org/feed/youtube-dl-updates-feed</id>\n        <updated>@TIMESTAMP@</updated>\n        @ENTRIES@\n    </feed>')
entry_template = textwrap.dedent('\n    <entry>\n        <id>https://yt-dl.org/feed/youtube-dl-updates-feed/youtube-dl-@VERSION@</id>\n        <title>New version @VERSION@</title>\n        <link href="http://ytdl-org.github.io/youtube-dl" />\n        <content type="xhtml">\n            <div xmlns="http://www.w3.org/1999/xhtml">\n                Downloads available at <a href="https://yt-dl.org/downloads/@VERSION@/">https://yt-dl.org/downloads/@VERSION@/</a>\n            </div>\n        </content>\n        <author>\n            <name>The youtube-dl maintainers</name>\n        </author>\n        <updated>@TIMESTAMP@</updated>\n    </entry>\n    ')
now = datetime.datetime.now()
now_iso = now.isoformat() + 'Z'
atom_template = atom_template.replace('@TIMESTAMP@', now_iso)
versions_info = json.load(open('update/versions.json'))
versions = list(versions_info['versions'].keys())
versions.sort()
entries = []
for v in versions:
    fields = v.split('.')
    year, month, day = map(int, fields[:3])
    faked = 0
    patchlevel = 0
    if len(fields) >= 4:
        try:
            patchlevel = int(fields[3])
        except ValueError:
            patchlevel = 1

    timestamp = '%04d-%02d-%02dT00:%02d:%02dZ' % (year, month, day, faked, patchlevel)
    entry = entry_template.replace('@TIMESTAMP@', timestamp)
    entry = entry.replace('@VERSION@', v)
    entries.append(entry)
else:
    entries_str = textwrap.indent(''.join(entries), '\t')
    atom_template = atom_template.replace('@ENTRIES@', entries_str)
# okay decompiling testbed_py/update-feed.py
