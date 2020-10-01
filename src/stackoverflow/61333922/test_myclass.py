import unittest
from unittest import mock
import serial
import myclass


class TestMyClass(unittest.TestCase):
    @mock.patch('myclass.serial.Serial')
    def test_do_something_fails_on_bad_write(self, mock_Serial):
        serial_instance = mock_Serial()
        serial_instance.write.return_value = 1
        want = -1
        dummy_data = b'123'
        c = myclass.MyClass('COM8', 115200)
        got = c.do_something(dummy_data)
        self.assertEqual(got, want)
        serial_instance.write.assert_called_once_with(b'123')

    @mock.patch('myclass.serial.Serial')
    def test_do_something_success(self, mock_Serial):
        serial_instance = mock_Serial()
        serial_instance.write.return_value = 3
        want = 0
        dummy_data = b'123'
        c = myclass.MyClass('COM8', 115200)
        got = c.do_something(dummy_data)
        self.assertEqual(got, want)
        serial_instance.write.assert_called_once_with(b'123')


if __name__ == '__main__':
    unittest.main()
