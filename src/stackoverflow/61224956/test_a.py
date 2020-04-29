import unittest
from unittest.mock import MagicMock, mock_open
from a import A


class TestA(unittest.TestCase):
    def test_fetch_data(self):
        engine_mock = MagicMock()
        trans = engine_mock.begin.return_value.__enter__.return_value
        trans.execute.return_value = 'fake data'
        a = A(engine_mock)
        a.fetch_data()
        engine_mock.begin.assert_called_once()
        trans.execute.assert_called_with("SELECT * FROM XXX")


if __name__ == '__main__':
    unittest.main()
