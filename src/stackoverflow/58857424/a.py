import datetime
from datetime import timedelta


class A():
    def _get_datetime(self, days):
        return (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')

    def do_something(self):
        date = self._get_datetime()
        return date
