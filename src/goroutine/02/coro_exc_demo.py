import unittest
from inspect import getgeneratorstate


class DemoException(Exception):
    """DemoException"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run')


class Test_demo_exc_handling(unittest.TestCase):
    def test_normal_workflow(self):
        exc_coro = demo_exc_handling()
        val = next(exc_coro)
        self.assertEqual(val, None)
        val = exc_coro.send(11)
        self.assertEqual(val, None)
        val = exc_coro.send(22)
        self.assertEqual(val, None)
        exc_coro.close()
        self.assertEqual(getgeneratorstate(exc_coro), 'GEN_CLOSED')

    def test_handle_demo_exception(self):
        exc_coro = demo_exc_handling()
        val = next(exc_coro)
        self.assertEqual(val, None)
        val = exc_coro.send(11)
        self.assertEqual(val, None)
        exc_coro.throw(DemoException)
        self.assertEqual(getgeneratorstate(exc_coro), 'GEN_SUSPENDED')

    def test_handle_unsupport_exception(self):
        exc_coro = demo_exc_handling()
        val = next(exc_coro)
        self.assertRaises(ZeroDivisionError, exc_coro.throw, ZeroDivisionError)
        self.assertEqual(getgeneratorstate(exc_coro), 'GEN_CLOSED')


unittest.main()
