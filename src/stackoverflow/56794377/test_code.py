from unittest import TestCase, main
from unittest.mock import patch
import code


class TestService(TestCase):
    def setUp(self):
        self.project_id = "sample-project-id"

    @patch('code.googleapiclient.discovery')
    def test__validate_event_with_empty_inputs(self, mock_discovery):
        # Arrange
        mock_discovery.build.return_value.zones.return_value.list.return_value.execute.return_value = {
            "items": [{"name": "eu-west-1"}]}

        # Act
        obj = code.Service(event={}, project=self.project_id)

        # Assert
        mock_discovery.build.assert_called_once_with('compute', 'v1', cache_discovery=False)
        mock_discovery.build.return_value.zones.assert_called_once()
        mock_discovery.build.return_value.zones.return_value.list.assert_called_once_with(project='sample-project-id')
        mock_discovery.build.return_value.zones.return_value.list.return_value.execute.assert_called_once()
        self.assertEqual(obj.zones, ["eu-west-1"])


if __name__ == '__main__':
    main()
