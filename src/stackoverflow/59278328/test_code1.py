import unittest
from unittest.mock import patch
from code1 import Foo
from code2 import Bar


class TestFoo(unittest.TestCase):
    @patch.object(Bar, 'bar_method', return_value='bar')
    def test_foo_method_shouldCallBarInstanceBarMethod(self, mock_bar_method):
        Foo.foo_method()
        mock_bar_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
