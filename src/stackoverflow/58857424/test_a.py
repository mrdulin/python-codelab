import unittest
from unittest.mock import patch
from datetime import datetime
from a import A

next_day = datetime.now().date()


class TestClass(unittest.TestCase):
    @patch.object(A, '_get_datetime', return_value=next_day)
    def test_do_something(self, mock_get_datetime):
        a_instance = A()
        actual = a_instance.do_something()
        self.assertEqual(actual, next_day)
        mock_get_datetime.assert_called_once()


if __name__ == '__main__':
    unittest.main()
