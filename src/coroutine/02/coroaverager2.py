import unittest
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


class TestAverager(unittest.TestCase):
    def test_normal_workflow(self):
        coro_avg = averager()
        next(coro_avg)
        coro_avg.send(10)
        coro_avg.send(30)
        coro_avg.send(6.5)
        try:
            coro_avg.send(None)
        except StopIteration as exc:
            result = exc.value
            self.assertTupleEqual(result, Result(count=3, average=15.5))


unittest.main()
