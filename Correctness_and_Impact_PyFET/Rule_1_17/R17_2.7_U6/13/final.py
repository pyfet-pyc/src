# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/fw_versions.py
# Compiled at: 2022-08-11 19:42:09
# Size of source mod 2**32: 350 bytes


def build_fw_dict(fw_versions, filter_brand=None):
    fw_versions_dict = defaultdict(set)
    for fw in fw_versions:
        if filter_brand is None or fw.brand == filter_brand:
            addr = fw.address
            sub_addr = fw.subAddress if fw.subAddress != 0 else None
            fw_versions_dict[(addr, sub_addr)].add(fw.fwVersion)
        return dict(fw_versions_dict)
# okay decompiling testbed_py/fw_versions.py
