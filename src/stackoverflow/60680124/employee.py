import requests


class Employee():
    def monthly_schedule(self):
        response = requests.get("http://www.google.com")
        if response.ok:
            return response.text
        else:
            return "Bad response"
