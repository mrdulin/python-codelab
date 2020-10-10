import unittest
from MyFileB import Bfunc
from unittest import mock


class TestMyFileB(unittest.TestCase):
    @mock.patch('MyFileB.A')
    def test_Bfunc(self, mock_A):
        a_instance = mock_A.return_value
        a_instance.Afunc.return_value = "mocked value"
        actual = Bfunc()
        self.assertEqual(actual, 'mocked value')
        mock_A.assert_called_once()
        a_instance.Afunc.assert_called_once()


if __name__ == '__main__':
    unittest.main()
