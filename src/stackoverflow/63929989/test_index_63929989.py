import unittest
from unittest import mock
from index_63929989 import my_func


class TestIndex(unittest.TestCase):
    @mock.patch('pandas.ExcelFile')
    def test_func(self, mock_pd_excelFile):
        mock_pd_excelFile.return_value.parse.return_value = 10
        actual = my_func()
        mock_pd_excelFile.assert_called_with('temp.xlsx')
        self.assertEqual(actual, 10)


if __name__ == '__main__':
    unittest.main()
