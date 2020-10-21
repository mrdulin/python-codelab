from azure.servicebus.control_client import ServiceBusService as AzureServiceBus


class AbcServiceBus:

    def __init__(self):
        self._namespace = '_namespace'
        self._topic_name = '_topic_name'
        self._service_bus = AzureServiceBus()

    def send_insert_notification(self, record_id):
        message_json = {'ids': [record_id]}
        self._service_bus.send_topic_message(
            namespace_name=self._namespace,
            topic_name=self._topic_name,
            message_json=message_json
        )
        return True
