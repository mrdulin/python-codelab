import unittest
from unittest.mock import patch, mock_open
from os_ex import pickle_wdir
from io import StringIO


class TestOsEx(unittest.TestCase):
    def test_pickle_wdir(self):
        fname = 'dir.pickle'
        m = mock_open(read_data='mocked data')
        with patch('os_ex.os') as mocked_obj, patch('builtins.open', m) as mocked_open, patch('pickle.dump') as mocked_dump:
            mocked_obj.getcwd.return_value = '/root'
            pickle_wdir(fname)
            mocked_obj.getcwd.assert_called()
            m.assert_called_with(fname, 'wb')
            handle = mocked_open()
            mocked_dump.assert_called_with('/root', handle)


if __name__ == '__main__':
    unittest.main()
