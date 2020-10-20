from unittest import TestCase, main
from unittest.mock import patch
from my_module_64443736 import bar


class TestCaseBar(TestCase):

    @patch('my_module_64443736.foo')
    def test_bar(self, mock_foo):
        def dynamicMock(i):
            if i == 'this':
                return 'teresa teng'
            else:
                return 'best singer'
        mock_foo.side_effect = dynamicMock
        items = ['this', 'that']
        result = bar(items)
        self.assertEqual(result, ['teresa teng', 'best singer'])
        self.assertTrue(mock_foo.call_count, 2)


if __name__ == '__main__':
    main()
