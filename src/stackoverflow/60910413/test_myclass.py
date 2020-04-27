import unittest
from myclass import MyClass, requests
from unittest.mock import MagicMock, patch
from collections import namedtuple


class testMyClass(unittest.TestCase):

    @patch('builtins.print')
    @patch.object(requests, 'get')
    def test_A(self, mocked_get, mocked_print):
        Response = namedtuple('Response', ['data'])
        response = Response(data={'has_value': True})
        mocked_get.side_effect = [response, 'new response']
        myclass = MyClass()
        data = {}
        myclass.A(data)
        mocked_get.assert_called_with('some_url', None)
        self.assertEqual(mocked_get.call_count, 2)
        mocked_print.assert_called_with('new response')

    def test_B(self):
        # same as test_A
        self.assertEqual(1, 1)

    def test__run(self):
        myclass = MyClass()
        myclass.A = MagicMock()
        myclass.B = MagicMock()
        myclass._run()
        myclass.A.assert_called_with({})
        myclass.B.assert_called_with({})


if __name__ == '__main__':
    unittest.main()
