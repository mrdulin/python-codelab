import unittest
from unittest.mock import patch
from Time import Time
from datetime import datetime


class TestTime(unittest.TestCase):
    @patch('Time.sleep', return_value=None)
    def test_sleepUntilMinuteDivisibleBy5(self, mock_sleep):
        Time.sleepUntilMinuteDivisibleBy5()
        mock_sleep.assert_called_with(100)


if __name__ == '__main__':
    unittest.main()
