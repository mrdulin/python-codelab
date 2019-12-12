import unittest
from base import BaseImporter
from unittest.mock import patch


class TestBaseImporter(unittest.TestCase):
    @patch('base.u', autospec=True)
    def test_run_importer(self, mock_u):
        base_importer = BaseImporter(folder_name='folder_name', source='source', table='table')
        mock_u.get_data_from_external_source.return_value = 'mocked data'
        base_importer.run_importer()
        mock_u.get_data_from_external_source.assert_called_once_with('source')
        mock_u.create_n_insert_into_sql.assert_called_once_with('table', 'mocked data')
        mock_u.create_n_insert_into_hive.assert_called_once_with('table', 'mocked data')
        mock_u.create_folder_hdfs.assert_called_once_with('folder_name')
