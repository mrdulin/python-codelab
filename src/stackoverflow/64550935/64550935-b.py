import time
import unittest
from unittest.mock import patch


class Tests(unittest.TestCase):
    def test_sleep(self):
        with patch("time.sleep") as sleepMock:
            time.sleep(0.01)
            sleepMock.assert_called_with(0.01)


if __name__ == '__main__':
    unittest.main()
