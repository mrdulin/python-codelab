import unittest


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("setting up")

    @unittest.skip("skip reason")
    def test_1(self):
        print("in test 1")

    def test_2(self):
        print("in test 2")


if __name__ == '__main__':
    unittest.main()
