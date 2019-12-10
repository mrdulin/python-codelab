import unittest
from unittest.mock import Mock, patch
import datetime
from my_calendar import get_today
from requests.exceptions import Timeout


def is_weekday():
    today = datetime.datetime.today()
    print(f'today: {today}')
    return (0 <= today.weekday() < 5)


requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)


class TestCalendar(unittest.TestCase):
    def tearDown(self):
        requests.reset_mock()

    @patch('my_calendar.datetime')
    def test_is_weekday(self, datetime_mock):
        datetime_mock.date.today = Mock(return_value=tuesday)
        self.assertEqual(get_today(), tuesday)
        datetime_mock.date.today = Mock(return_value=saturday)
        self.assertEqual(get_today(), saturday)
        datetime_mock.date.today.assert_called()

    def test_is_weekday(self):
        self.skipTest('todo')
        datetime.datetime.today.return_value = tuesday
        self.assertTrue(is_weekday())

        datetime.datetime.today.return_value = saturday
        self.assertFalse(is_weekday())

    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        self.assertEqual(get_holidays()['12/25'], 'Christmas')

    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        self.assertEqual(get_holidays()['12/25'], 'Christmas')
        # Finally, assert .get() was called twice
        self.assertEqual(requests.get.call_count, 2)


unittest.main(verbosity=2)
