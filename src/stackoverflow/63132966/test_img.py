import unittest
from unittest import mock
from img import Img


class TestImg(unittest.TestCase):
    @mock.patch('img.Image')
    def test_close(self, mock_Image):
        my_img = Img()
        my_img.close()
        mock_Image.Image.close.assert_called_once_with('123')


if __name__ == '__main__':
    unittest.main()
