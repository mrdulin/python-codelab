from get_table import get_table_name
from unittest.mock import patch
import unittest


class TestFetchTable(unittest.TestCase):
    @patch('get_table.requests')
    def test_get_table_name(self, mock_requests):
        mock_requests.get.return_value = 'table_1'
        result = get_table_name('id1')
        self.assertEqual(result, 'table_1')


if __name__ == '__main__':
    unittest.main()
