import unittest
from unittest import mock
from unittest.mock import Mock
from gcs import GCSObject


class TestGCSObject(unittest.TestCase):
    @mock.patch('gcs.storage')
    def test_read(self, mock_storage):
        mock_gcs_client = mock_storage.Client.return_value
        mock_bucket = Mock()
        mock_bucket.blob.return_value.download_as_string.return_value = "teresa teng".encode('utf-8')
        mock_gcs_client.bucket.return_value = mock_bucket
        gcs = GCSObject('fake_path')
        actual = gcs.read()
        mock_storage.Client.assert_called_once()
        mock_gcs_client.bucket.assert_called_once_with('fake_path')
        mock_bucket.blob.assert_called_once_with('')
        mock_bucket.blob.return_value.download_as_string.assert_called_once()
        self.assertEqual(actual, "teresa teng".encode('utf-8'))

    @mock.patch('gcs.storage')
    def test_write(self, mock_storage):
        mock_gcs_client = mock_storage.Client.return_value
        mock_bucket = Mock()
        mock_gcs_client.get_bucket.return_value = mock_bucket
        gcs = GCSObject('fake_path')
        gcs.write(b'teresa teng')
        mock_storage.Client.assert_called_once()
        mock_gcs_client.get_bucket.assert_called_once_with('fake_path')
        mock_bucket.blob.assert_called_once_with('')
        mock_bucket.blob.return_value.upload_from_string.assert_called_once_with(b'teresa teng')


if __name__ == '__main__':
    unittest.main()
