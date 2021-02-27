import requests
from typing import Dict

import ledgerx
from ledgerx.util import gen_headers, gen_url


class HttpClient:
    @staticmethod
    def get(url: str, params: Dict = {}, include_api_key: bool = False):
        headers = gen_headers(include_api_key)
        res = requests.get(url, headers=headers, params=params)
        return res

    @staticmethod
    def post(url: str, data: Dict = {}, include_api_key: bool = False):
        headers = gen_headers(include_api_key)
        res = requests.post(url, headers=headers, json=data)
        return res