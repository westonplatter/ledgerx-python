import requests
from typing import Dict


class Client:
    def __init__(self):
        pass

    def get(self, url, headers, params={}):
        return requests.get(url, headers=headers, params=params)

    def post(self, url, headers, data):
        return requests.post(url, headers=headers, json=data)
