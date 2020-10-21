import unittest
from unittest import mock
from azure_service_bus import AbcServiceBus


class TestAbcServiceBus(unittest.TestCase):
    def test_send_insert_notification(self):
        record_id = '1'

        with mock.patch('azure_service_bus.AzureServiceBus') as mock_AzureServiceBus:
            mock_AzureServiceBus_instance = mock_AzureServiceBus.return_value
            sb = AbcServiceBus()
            actual = sb.send_insert_notification(record_id)
            self.assertTrue(actual)
            mock_AzureServiceBus.assert_called_once()
            mock_AzureServiceBus_instance.send_topic_message.assert_called_with(
                namespace_name='_namespace',
                topic_name='_topic_name',
                message_json={'ids': ['1']}
            )


if __name__ == '__main__':
    unittest.main()
