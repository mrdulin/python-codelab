import unittest
from func import func
from unittest.mock import MagicMock


class TestFunc(unittest.TestCase):
    def test_func(self):
        query_res = [("name_1", "value_1"), ("name_2", "value_2")]
        expected_vals = ["value_1", "value_2"]
        db_engine = MagicMock()
        execute = db_engine.execute.return_value
        execute.fetchall.return_value = query_res
        vals = func(db_engine)

        db_engine.execute.assert_called_with("SELECT * FROM table")
        execute.fetchall.assert_called_once()
        self.assertEqual(expected_vals, vals)


if __name__ == '__main__':
    unittest.main()
