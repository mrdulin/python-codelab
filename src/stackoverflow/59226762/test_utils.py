import unittest
from unittest.mock import Mock
import utils


class TestUtils(unittest.TestCase):
    def test_get_client_object(self):
        dbconnection = Mock(name="dbconnection")
        mycursor = Mock(name="mycursor")
        mycursor.fetchall.return_value = "testing_return_value"
        dbconnection.cursor.return_value = mycursor

        self.assertEqual("testing_return_value",
                         utils.query_db(dbconnection, 12345))
        dbconnection.cursor.assert_called_once()
        mycursor.execute.assert_called_once_with(12345)
        mycursor.fetchall.assert_called_once()

    def test_query_db_exception(self):
        dbconnection = Mock(name="dbconnection")
        mycursor = Mock(name="mycursor")
        mycursor.fetchall.side_effect = Exception
        dbconnection.cursor.return_value = mycursor

        with self.assertRaises(Exception):
            utils.query_db(dbconnection, 12345)


if __name__ == '__main__':
    unittest.main(verbosity=2)
