# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_async_case.py
# Compiled at: 2022-08-11 20:18:41
# Size of source mod 2**32: 996 bytes


def test_exception_in_setup(self):

    class Test(unittest.IsolatedAsyncioTestCase):

        async def asyncSetUp(self):
            events.append('asyncSetUp')
            self.addAsyncCleanup(self.on_cleanup)
            raise MyException()

        async def test_func(self):
            events.append('test')

        async def asyncTearDown(self):
            events.append('asyncTearDown')

        async def on_cleanup(self):
            events.append('cleanup')

    events = []
    test = Test('test_func')
    result = test.run()
    self.assertEqual(events, ['asyncSetUp', 'cleanup'])
    self.assertIs(result.errors[0][0], test)
    self.assertIn('MyException', result.errors[0][1])
    events = []
    test = Test('test_func')
    try:
        test.debug()
    except MyException:
        pass
    else:
        self.fail('Expected a MyException exception')
    self.assertEqual(events, ['asyncSetUp'])
    test.doCleanups()
    self.assertEqual(events, ['asyncSetUp', 'cleanup'])
# okay decompiling testbed_py/test_async_case.py
