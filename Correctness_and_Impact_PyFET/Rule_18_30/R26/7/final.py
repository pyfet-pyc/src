# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-12 03:02:43
pass
# okay decompiling testbed_py/final.py
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:02:11
# Size of source mod 2**32: 993 bytes


def main():
    if '--interactive' in sys.argv:
        import ansible.module_utils.basic
        ansible.module_utils.basic._ANSIBLE_ARGS = json.dumps(dict(ANSIBLE_MODULE_ARGS=dict(fail_mode='graceful')))
    module = AnsibleModule(argument_spec=dict(fail_mode=dict(type='list', default=['success'])))
    result = dict(changed=True)
    fail_mode = module.params['fail_mode']
    try:
        if 'leading_junk' in fail_mode:
            print('leading junk before module output')
        if 'graceful' in fail_mode:
            module.fail_json(msg='failed gracefully')
        if 'exception' in fail_mode:
            raise Exception('failing via exception')
        if 'stderr' in fail_mode:
            print('printed to stderr', file=(sys.stderr))
        (module.exit_json)(**result)
    finally:
        if 'trailing_junk' in fail_mode:
            print('trailing junk after module output')
# okay decompiling testbed_py/test.py
# decompiled 2 files: 2 okay, 0 failed
