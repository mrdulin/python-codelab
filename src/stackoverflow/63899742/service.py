import json
import requests
from collections import namedtuple

external = namedtuple('URL', 'URL')
external = external('http://localhost:3000/api/')


def create_user(name):
    headers = {}
    url = external.URL + 'user/'
    payload = {
        "name": name
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()
