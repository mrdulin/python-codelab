import unittest


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
    def test_averager(self):
        coro_avg = averager()
        val = next(coro_avg)
        self.assertEqual(val, None)
        val = coro_avg.send(10)
        self.assertEqual(val, 10)
        val = coro_avg.send(30)
        self.assertEqual(val, 20)
        val = coro_avg.send(5)
        self.assertEqual(val, 15)
        coro_avg.close()


unittest.main()
