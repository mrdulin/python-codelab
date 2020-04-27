import unittest
from unittest.mock import patch
from worker import Worker


class TestWorker(unittest.TestCase):
    def test_work(self):
        with patch('worker.Helper') as mock_Helper:
            mock_helper_instance = mock_Helper.return_value
            mock_helper_instance.get_path.return_value = 'testing'
            worker = Worker()
            mock_Helper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')


if __name__ == '__main__':
    unittest.main()
