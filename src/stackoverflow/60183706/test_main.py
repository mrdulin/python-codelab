from main import MyClass
import unittest
from unittest.mock import mock_open, patch


class TestMain(unittest.TestCase):
    def test_get_version(self):
        m = mock_open(read_data='version= 1.0.0')
        with patch('builtins.open', m) as mocked_open:
            myclass_instace = MyClass()
            version = myclass_instace.get_version()
            self.assertEqual(version, '1.0.0')
            m.assert_called_with('file_path')


if __name__ == '__main__':
    unittest.main()
