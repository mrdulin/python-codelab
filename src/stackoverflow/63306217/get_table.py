
import requests


def get_table_name(id):
    url = "https://some_api" + id
    table = requests.get(url)
    return table
