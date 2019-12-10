import unittest
from worker import Worker
from unittest.mock import Mock


class TestWorker(unittest.TestCase):
    def test_set_processor(self):
        mock_processor = Mock()
        worker = Worker()
        worker.set_processor(mock_processor)
        assert worker._processor == mock_processor
        worker.start_work(b'')
        mock_processor.parse.assert_called_once_with(b'')


if __name__ == '__main__':
    unittest.main()
