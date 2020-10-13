import unittest
import json
from app import get_json_data
from unittest.mock import Mock


class TestDoSessionGet(unittest.TestCase):

    def test_should_mock_session_get(self):
        data = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }
        mock_session = Mock()
        mock_response = Mock()
        mock_session.get.return_value = mock_response
        mock_response.json.return_value = data

        response = get_json_data('https://jsonplaceholder.typicode.com/todos/1', mock_session)

        mock_session.get.assert_called_once_with('https://jsonplaceholder.typicode.com/todos/1')
        mock_response.raise_for_status.assert_called_once()
        mock_response.json.assert_called_once()
        self.assertEqual(response, data)


if __name__ == '__main__':
    unittest.main()
