# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/add-version.py
# Compiled at: 2022-08-08 20:30:13
# Size of source mod 2**32: 1170 bytes
from __future__ import unicode_literals
import json, sys, hashlib, os.path
if len(sys.argv) <= 1:
    print('Specify the version number as parameter')
    sys.exit()
version = sys.argv[1]
with open('update/LATEST_VERSION', 'w') as (f):
    f.write(version)
versions_info = json.load(open('update/versions.json'))
if 'signature' in versions_info:
    del versions_info['signature']
new_version = {}
filenames = {'bin':'youtube-dl', 
 'exe':'youtube-dl.exe', 
 'tar':'youtube-dl-%s.tar.gz' % version}
build_dir = os.path.join('..', '..', 'build', version)
for key, filename in filenames.items():
    url = 'https://yt-dl.org/downloads/%s/%s' % (version, filename)
    fn = os.path.join(build_dir, filename)
    with open(fn, 'rb') as (f):
        data = f.read()
    if not data:
        raise ValueError('File %s is empty!' % fn)
    sha256sum = hashlib.sha256(data).hexdigest()
    new_version[key] = (url, sha256sum)
else:
    versions_info['versions'][version] = new_version
    versions_info['latest'] = version
    with open('update/versions.json', 'w') as (jsonf):
        json.dump(versions_info, jsonf, indent=4, sort_keys=True)
# okay decompiling testbed_py/add-version.py
