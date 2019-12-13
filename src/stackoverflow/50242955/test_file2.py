import unittest
from unittest.mock import patch
from file2 import MyClass


class TestMyClass(unittest.TestCase):
    @patch('file2.file1')
    def test_calculate(self, mock_file1):
        inst = mock_file1.SomeHelper.return_value
        inst.my_var = 0.5
        to_test = MyClass.calculate()
        self.assertTrue(to_test)
        mock_file1.SomeHelper.assert_called_once()

    @patch('file2.file1')
    def test_calculate_2(self, mock_file1):
        inst = mock_file1.SomeHelper.return_value
        inst.my_var = 2
        to_test = MyClass.calculate()
        self.assertFalse(to_test)
        mock_file1.SomeHelper.assert_called_once()


if __name__ == '__main__':
    unittest.main()
