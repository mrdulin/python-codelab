import unittest
from unittest import mock
from content_provider import ContentReportGeneralSearch


class TestContentProvider(unittest.TestCase):
    @mock.patch('content_provider.ContentUser')
    def test_getReport(self, mock_ContentUser):
        content_user_instance = mock_ContentUser.return_value
        provider = ContentReportGeneralSearch()
        provider.getReport(username='test', search_text='')
        content_user_instance.getUserRef.assert_called_once_with(username='test')


if __name__ == '__main__':
    unittest.main()
