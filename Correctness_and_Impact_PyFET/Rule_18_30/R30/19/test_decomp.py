# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:53:47


def test_header_split():
    unchanged = '\n    python/:list\n    ls\n    +\n    g++\n    g/+\n    clang++\n    btrfs~volume\n    :intro\n    :cht.sh\n    python/copy+file\n    python/rosetta/:list\n    emacs:go-mode/:list\n    g++g++\n    '
    split = '\n    python copy file\n    python/copy file\n\n    python  file\n    python/file\n\n    python+file\n    python/file\n\n    g++ -O1\n    g++/-O1\n    '
    inp, outp = test.split('\n')
    assert outp == _add_section_name(inp), '_add_section_name'
# okay decompiling testbed_py/test.py
