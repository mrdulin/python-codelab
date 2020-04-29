import unittest
from unittest.mock import patch
from main import main


def mock_load_data(name="order"):
    if name == "order":
        return 1
    elif name == "product":
        return 2


class TestMain(unittest.TestCase):
    @patch('main.load_data', side_effect=mock_load_data)
    def test_main(self, mock_load_data):
        rval1 = main('order')
        self.assertEqual(rval1, 1)
        rval2 = main('product')
        self.assertEqual(rval2, 2)


if __name__ == '__main__':
    unittest.main()
