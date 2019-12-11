import unittest
from unittest.mock import Mock, patch, mock_open, call
from GitRepoParser import GitRepoParser, os


class GitRepoParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = GitRepoParser('/path-to-download')
        self.mock_open = mock_open(read_data='some data')

    def test_get_folder_path(self):
        folder_path = self.parser.get_folder_path(service_name='oleg-service')
        self.assertIsInstance(folder_path, str)

    @patch('GitRepoParser.os')
    def test_create_new_service_read_and_write_file_correctly(self, mock_os):
        mock_path = Mock()
        mock_path.dirname.return_value = '/Users/foo'
        mock_path.isdir.return_value = False
        mock_path.join.return_value = '/Users/whatever'
        mock_path.isfile.return_value = True
        mock_os.path = mock_path
        mock_os.makedirs = Mock()

        with patch('GitRepoParser.open', self.mock_open):
            self.parser.create_new_service(service_name='oleg-service', service_version='1.0')
            mock_path.isdir.assert_called_with('/path-to-download/configuration/settings/oleg-service')
            mock_os.makedirs.assert_called_with('/path-to-download/configuration/settings/oleg-service')
            expected = [call('/Users/whatever', 'r'),
                        call('/path-to-download/configuration/settings/oleg-service/oleg-service-deployment.properties', 'w')]
            self.mock_open.assert_has_calls(expected)
            handle = self.mock_open()
            handle.write.assert_called()
            handle.close.assert_called_once()

    @patch('GitRepoParser.os')
    def test_create_new_service_do_nothing_if_dir_path_is_dir(self, mock_os):
        mock_path = Mock()
        mock_path.isdir.return_value = True
        mock_os.path = mock_path
        mock_os.makedirs = Mock()

        self.parser.create_new_service(service_name='oleg-service', service_version='1.0')
        mock_path.isdir.assert_called_with('/path-to-download/configuration/settings/oleg-service')
        mock_os.makedirs.assert_not_called()


if __name__ == '__main__':
    unittest.main()
