import requests
from typing import Dict

import ledgerx
from ledgerx.util import gen_headers, gen_url


class HttpClient:
    @staticmethod
    def get(url: str, params: Dict = {}):
        headers = gen_headers()
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def post(url: str, data: Dict = {}):
        headers = gen_headers()
        return requests.post(url, headers=headers, json=data)
