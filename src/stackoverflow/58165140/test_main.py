import unittest
from main import change_from, os
from unittest.mock import patch


class TestMain(unittest.TestCase):

    def test_change_from(self):
        with patch.object(os, 'popen') as mock_popen:
            Lines = ['43', '45', '47', '50', '51', '52', '53', '54', '55']
            mock_popen().readlines.return_value = Lines
            lineTag = "undocumented_line:"
            self.assertEqual(change_from(lineTag), [])
            mock_popen.assert_called_with('ls -al')
            mock_popen().readlines.assert_called_once()


if __name__ == '__main__':
    unittest.main()
