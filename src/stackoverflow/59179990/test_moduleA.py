import unittest
from unittest.mock import patch, call
from moduleA import A


class TestA(unittest.TestCase):
    @patch("moduleA.B")
    def test_A(self, mockB):
        A()
        mockB.assert_has_calls([
            call(1, 2),
            call(3, 4)
        ])


if __name__ == '__main__':
    unittest.main()
