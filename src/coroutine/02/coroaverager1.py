import unittest
from coroutil import coroutine
from inspect import getgeneratorstate


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


class TestAverager(unittest.TestCase):
    def test_normal_workflow_with_decorator(self):
        coro_avg = averager()
        self.assertEqual(getgeneratorstate(coro_avg), 'GEN_SUSPENDED')
        val = coro_avg.send(10)
        self.assertEqual(val, 10)
        self.assertEqual(getgeneratorstate(coro_avg), 'GEN_SUSPENDED')
        val = coro_avg.send(30)
        self.assertEqual(val, 20)
        val = coro_avg.send(5)
        self.assertEqual(val, 15)
        coro_avg.close()
        self.assertEqual(getgeneratorstate(coro_avg), 'GEN_CLOSED')

    def test_exception_handling(self):
        coro_avg = averager()
        val = coro_avg.send(10)
        self.assertEqual(val, 10)
        self.assertRaises(TypeError, coro_avg.send, 'spam')
        self.assertRaises(StopIteration, coro_avg.send, 20)


unittest.main()
