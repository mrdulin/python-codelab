import unittest
from side_eff import Backend
from unittest.mock import patch


class TestBackendConnection(unittest.TestCase):

    def test_connection_waiting(self):
        """Test that the backend waits for connection untill the handler connects"""
        with patch('side_eff.Handler') as MockHandler:
            handlerInstance = MockHandler.return_value
            handlerInstance.is_connected.side_effect = [False] * 4 + [True]
            bknd = Backend()
            bknd.initConnection()
            self.assertEqual(handlerInstance.is_connected.call_count, 5)


if __name__ == '__main__':
    unittest.main()
