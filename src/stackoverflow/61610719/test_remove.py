from os import remove
import unittest
from unittest.mock import patch


class TestRemove(unittest.TestCase):
    def test_patch_remove(self):
        with patch("os.remove") as mocked_remove:
            mocked_remove('foo')
            mocked_remove.assert_called_with('foo')


if __name__ == '__main__':
    unittest.main()
