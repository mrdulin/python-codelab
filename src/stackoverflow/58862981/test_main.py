import unittest
from main import AADatabase
from unittest.mock import patch


class TestAADatabase(unittest.TestCase):
    def test_database_inaccessible(self):
        with patch.object(AADatabase, 'is_primary') as is_primary_mocked:
            is_primary_mocked.return_value = True
            res = AADatabase.run()
            self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
