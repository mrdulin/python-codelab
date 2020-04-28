from main import my_func
import unittest
from unittest.mock import patch


class TestMain(unittest.TestCase):
    @patch('main.MyClass')
    def test_my_func(self, MockMyClass):
        mock_my_class_instance = MockMyClass.return_value
        my_func()
        mock_my_class_instance.do_thing.assert_called_once()


if __name__ == '__main__':
    unittest.main()
