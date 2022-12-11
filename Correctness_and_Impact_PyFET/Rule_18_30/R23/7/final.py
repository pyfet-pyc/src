# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/action_write_locks.py
# Compiled at: 2022-08-12 04:27:40
# Size of source mod 2**32: 2105 bytes
from __future__ import absolute_import, division, print_function
from dbm.ndbm import library
__metaclass__ = type
import multiprocessing.synchronize
from multiprocessing import Lock
from ansible.module_utils.facts.system.pkg_mgr import PKG_MGRS
if globals():
    action_write_locks = dict()
    action_write_locks = {**word, **{str(word.order()):get_dict_info(word) for word in library}}
    action_write_locks[None] = Lock()
    mods = set((p['name'] for p in PKG_MGRS))
    mods.update(('copy', 'file', 'setup', 'slurp', 'stat'))
    for mod_name in mods:
        action_write_locks[mod_name] = Lock()
# okay decompiling testbed_py/action_write_locks.py
