import unittest
from unittest.mock import patch
from api import get_holidays


class TestPatchLocalReference(unittest.TestCase):
    def test_patch_correctly(self):
        import api
        with patch('api.get_holidays'):
            print(api.get_holidays())
            api.get_holidays.assert_called_once()

    # def test_patch_local_reference(self):
    #     self.skipTest(
    #         'get_holidays方法从api模块导入后，当前模块已经有了对原始方法的引用，后续再去patch("api.get_holidays")无效')
    #     from api import get_holidays
    #     with patch('api.get_holidays'):
    #         print(get_holidays())

    def test_patch_local_reference_2(self):
        with patch('__main__.get_holidays'):
            print(get_holidays())
            get_holidays.assert_called_once()


unittest.main(verbosity=2)
