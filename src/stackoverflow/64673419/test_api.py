import unittest
from unittest import mock
from api import download_models


class EmbeddingAPITest(unittest.TestCase):

    @mock.patch('api.gcsfs.GCSFileSystem')
    def test_download_models(self, mock_filesystem):
        mock_filesystem.return_value.get.return_value = []
        download_models('gcs_model_path', 'local_path')
        mock_filesystem.assert_called_once_with(project="teresa.teng")
        mock_filesystem.return_value.get.assert_called_once_with('gcs_model_path', 'local_path', recursive=True)


if __name__ == '__main__':
    unittest.main()
