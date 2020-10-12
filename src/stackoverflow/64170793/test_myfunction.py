import unittest
from unittest import mock
import myfunction


class TestMyFunctionModule(unittest.TestCase):
    @mock.patch('myclass.MyClass')
    def test_my_function(self, mock_my_class):
        myclassInstanceMocks = [mock.Mock(name='a'), mock.Mock(name='b')]
        myclassInstanceMocks[0].get_value.return_value = 4
        myclassInstanceMocks[1].get_value.return_value = 5
        mock_my_class.side_effect = myclassInstanceMocks
        exp_result = 9
        result = myfunction.my_function()
        self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main()
