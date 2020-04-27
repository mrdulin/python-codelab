import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.e1 = Employee()

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.e1.monthly_schedule()
            mocked_get.assert_called_with("http://www.google.com")

            self.assertEqual(schedule, "Success")


if __name__ == '__main__':
    unittest.main()
