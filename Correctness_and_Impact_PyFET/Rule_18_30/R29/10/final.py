# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 09:11:07
# Size of source mod 2**32: 964 bytes


class TestLambdaAPI(unittest.TestCase):
    CODE_SIZE = 50
    CODE_SHA_256 = '/u60ZpAA9bzZPVwb8d4390i5oqP1YAObUwV03CZvsWA='
    UPDATED_CODE_SHA_256 = '/u6A='
    MEMORY_SIZE = 128
    ROLE = 'arn:aws:iam::123456:role/role-name'
    LAST_MODIFIED = datetime.datetime.utcnow()
    TRACING_CONFIG = {'Mode': 'PassThrough'}
    REVISION_ID = 'e54dbcf8-e3ef-44ab-9af7-8dbef510608a'
    HANDLER = 'index.handler'
    RUNTIME = 'node.js4.3'
    TIMEOUT = 60
    FUNCTION_NAME = 'test1'
    ALIAS_NAME = 'alias1'
    ALIAS2_NAME = 'alias2'
    RESOURCENOTFOUND_EXCEPTION = 'ResourceNotFoundException'
    RESOURCENOTFOUND_MESSAGE = 'Function not found: %s'
    ALIASEXISTS_EXCEPTION = 'ResourceConflictException'
    ALIASEXISTS_MESSAGE = 'Alias already exists: %s'
    ALIASNOTFOUND_EXCEPTION = 'ResourceNotFoundException'
    ALIASNOTFOUND_MESSAGE = 'Alias not found: %s'
    TEST_UUID = 'Test'
    TAGS = {'hello', 'world', 'env', 'prod'}
# okay decompiling testbed_py/test.py
