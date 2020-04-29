import unittest
from unittest.mock import patch
from main import main
from someClass import SomeClass


class TestMain(unittest.TestCase):
    # @patch('main.SomeClass', spec=SomeClass)
    # def test_main(self, mock_SomeClass):
    #     """test mock with specification
    #     The get_name method doesn't exist anymore, it will raise an attribute error
    #     """
    #     msc_instance = mock_SomeClass.return_value
    #     msc_instance.get_name.return_value = 'elsa'
    #     actual = main()
    #     self.assertEqual(actual, 'elsa')

    @patch('main.SomeClass')
    def test_main_2(self, mock_SomeClass):
        """If don't provide a spec, even though the get_name method is removed from SomeClass, this test case still pass.
        But it shouldn't pass.
        """
        msc_instance = mock_SomeClass.return_value
        msc_instance.get_name.return_value = 'elsa'
        actual = main()
        self.assertEqual(actual, 'elsa')


if __name__ == '__main__':
    unittest.main()
