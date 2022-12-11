# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/cheat_wrapper_test.py
# Compiled at: 2022-08-08 20:31:53
# Size of source mod 2**32: 558 bytes
from cheat_wrapper import _add_section_name
unchanged = '\npython/:list\nls\n+\ng++\ng/+\nclang++\nbtrfs~volume\n:intro\n:cht.sh\npython/copy+file\npython/rosetta/:list\nemacs:go-mode/:list\ng++g++\n'
split = '\npython copy file\npython/copy file\n\npython  file\npython/file\n\npython+file\npython/file\n\ng++ -O1\ng++/-O1\n'

def test_header_split():
    for inp in unchanged.strip().splitlines():
        assert inp == _add_section_name(inp)
    else:
        for test in split.strip().split('\n\n'):
            inp, outp = test.split('\n')
            assert outp == _add_section_name(inp)
# okay decompiling testbed_py/cheat_wrapper_test.py
