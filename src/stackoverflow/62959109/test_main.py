import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from main import Blog


class TestBlog(TestCase):
    @patch('main.requests')
    def test_blog_posts(self, mock_requests):
        mock_requests.get.return_value.json.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]
        blog = Blog('teresa teng')
        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        mock_requests.get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts')
        mock_requests.get.return_value.json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
