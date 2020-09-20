import unittest
from unittest.mock import Mock
from collections import namedtuple
from myclass_63948475 import MyClass

Image = namedtuple('Image', ['regions'])
Region = namedtuple('Region', 'region_id')


class TestMyClass(unittest.TestCase):

    def test_method_to_test(self):

        regions = [Region('1'), Region('2'), Region('3')]
        images = [Image(regions=regions)]
        mock_client = Mock()
        mock_client.get_stuff.return_value = images
        myclass = MyClass(mock_client)
        actual = myclass.method_to_test()
        mock_client.get_stuff.assert_called_once()
        self.assertEqual(actual, ['1', '2', '3'])


if __name__ == '__main__':
    unittest.main()
