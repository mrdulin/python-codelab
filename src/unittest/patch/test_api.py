import unittest
from api import get_holidays, requests
from requests.exceptions import Timeout
from unittest.mock import patch


class TestApi(unittest.TestCase):
    @patch('api.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        mock_requests.get.assert_called_once_with(
            'http://localhost/api/holidays')

    def test_get_holidays_timeout_2(self):
        with patch('api.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get_holidays.assert_called_once_with(
                    'http://localhost/api/holidays')

    @patch.object(requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout_3(self, mock_requests):
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once_with(
                'http://localhost/api/holidays')


unittest.main(verbosity=2)
