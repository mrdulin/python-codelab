import requests


class MyClass:
    def A(self, data):
        params = None
        response = requests.get("some_url", params)
        if response.data["has_value"]:
            new_response = requests.get("some_url", params)
            print(new_response)

    def B(self, data):
        params = None
        response = requests.get("some_url", params)

    def _run(self):
        data = {}
        self.A(data)
        self.B(data)
