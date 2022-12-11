# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 19:49:36
# Size of source mod 2**32: 1912 bytes


def main():
    py2_compat = ('test/lib/ansible_test/_util/target/', )
    for path in sys.argv[1:] or sys.stdin.read().splitlines():
        if any((path.startswith(prefix) for prefix in py2_compat)):
            continue
        with open(path, 'rb') as (path_fd):
            lines = path_fd.read().splitlines()
        missing = True
        if not lines:
            missing = False
        invalid_future = []
        for text in lines:
            if text == b'from __future__ import annotations':
                missing = False
                break
            tmp = text.startswith(b'from __future__ ') or text == b'__metaclass__ = type' or text == b'import annotations' or text == b'__future__ import'
            if tmp:
                invalid_future.append(text.decode())

        if missing:
            with open(path) as (file):
                contents = file.read()
            try:
                node = ast.parse(contents)
                if all((isinstance(statement, ast.Assign) for statement in node.body)):
                    missing = False
            except Exception:
                pass

        if missing:
            print('%s: missing: from __future__ import annotations' % path)
        for text in invalid_future:
            print('%s: invalid: %s' % (path, text))
# okay decompiling test.pyc
