# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 21:00:49
# Size of source mod 2**32: 1386 bytes
from __future__ import absolute_import, division, print_function
__metaclass__ = type
import json, sys
from ansible_collections.testns.testcoll.plugins.module_utils import leaf, secondary
import ansible_collections.testns.testcoll.plugins.module_utils.subpkg_with_init as spwi_thingtocall
import ansible_collections.testns.testcoll.plugins.module_utils.subpkg_with_init as spwi_submod_thingtocall
import ansible_collections.testns.testcoll.plugins.module_utils.subpkg_with_init as spwi_cousin_submod_thingtocall

def main():
    mu_result = leaf.thingtocall()
    mu2_result = secondary.thingtocall()
    mu3_result = 'thingtocall in subpkg.submod'
    mu4_result = spwi_thingtocall()
    mu5_result = spwi_submod_thingtocall()
    mu6_result = spwi_cousin_submod_thingtocall()
    print(json.dumps(dict(changed=False, source='user', mu_result=mu_result, mu2_result=mu2_result, mu3_result=mu3_result,
      mu4_result=mu4_result,
      mu5_result=mu5_result,
      mu6_result=mu6_result)))
    sys.exit()


if __name__ == '__main__':
    main()
# okay decompiling test.pyc
