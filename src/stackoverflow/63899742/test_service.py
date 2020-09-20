import unittest
import requests
from service import create_user
from unittest.mock import patch, Mock
import json


class TestService(unittest.TestCase):
    @patch.object(requests, 'post')
    def test_create_user(self, mock_post):
        mock_json = Mock()
        mock_json.return_value = 'mock data'
        mock_post.return_value.json = mock_json
        actual = create_user("teresa teng")
        mock_post.assert_called_with('http://localhost:3000/api/user/', headers={},
                                     data=json.dumps({"name": "teresa teng"}))
        self.assertEqual(actual, 'mock data')


if __name__ == '__main__':
    unittest.main()
