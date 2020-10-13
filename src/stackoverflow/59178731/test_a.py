import unittest
from unittest import mock


class TestA(unittest.TestCase):
    @mock.patch('arg.ToBeMocked')
    def test__init__(self, mock_ToBeMocked):
        mock_ToBeMocked.return_value = 'Love Teresa Teng'
        from a import A
        a_instance = A()
        self.assertEqual(a_instance.arg, 'Love Teresa Teng')
        mock_ToBeMocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
