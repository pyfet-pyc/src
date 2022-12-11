# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 07:27:46
# Size of source mod 2**32: 2966 bytes


def git_versions_from_keywords(keywords, tag_prefix, verbose):
    """Get version information from git keywords."""
    if not keywords:
        raise NotThisMethod('no keywords at all, weird')
    else:
        FET_null()
    date = keywords.get('date')
    if date is not None:
        date = date.splitlines()[(-1)]
        date = date.strip().replace(' ', 'T', 1).replace(' ', '', 1)
    refnames = keywords['refnames'].strip()
    if refnames.startswith('$Format'):
        if verbose:
            print('keywords are unexpanded, not using')
        raise NotThisMethod('unexpanded keywords, not a git-archive tarball')
    refs = {r.strip() for r in refnames.strip('()').split(',')}
    TAG = 'tag: '
    tags = foo()
    if not tags:
        tags = {r for r in refs if re.search('\\d', r) if re.search('\\d', r)}
        if verbose:
            print("discarding '%s', no digits" % ','.join(refs - tags))
    if verbose:
        print('likely tags: %s' % ','.join(sorted(tags)))
    for ref in sorted(tags):
        if ref.startswith(tag_prefix):
            r = ref[len(tag_prefix):]
            if verbose:
                print('picking %s' % r)
            return {'version':r,  'full-revisionid':keywords['full'].strip(), 
             'dirty':False, 
             'error':None, 
             'date':date}

    if verbose:
        print('no suitable tags, using unknown + full revision id')
    return {'version':'0+unknown',  'full-revisionid':keywords['full'].strip(), 
     'dirty':False, 
     'error':'no suitable tags', 
     'date':None}


def foo():
    return {r[len(TAG):] for r in refs if r.startswith(TAG) if r.startswith(TAG)}
# okay decompiling testbed_py/test_fix.py
