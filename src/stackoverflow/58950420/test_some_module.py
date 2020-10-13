import unittest
from unittest.mock import patch
from some_module import SomeModule


class TestSomeModule(unittest.TestCase):
    @patch.object(SomeModule, 'c')
    @patch.object(SomeModule, 'b')
    @patch.object(SomeModule, 'a')
    def test_bring_them_altogether(self, mock_a, mock_b, mock_c):
        SomeModule.bring_them_altogether()
        mock_a.assert_called_once()
        mock_b.assert_called_once()
        mock_c.assert_called_once()


if __name__ == '__main__':
    unittest.main()
