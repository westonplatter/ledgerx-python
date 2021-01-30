from typing import Dict
from ledgerx.client import Client
from ledgerx.util import gen_headers


class TraderBlotter:
    @staticmethod
    def next(next_url: str):
        client = Client()
        headers = gen_headers()
        res = client.get(next_url, headers)
        return res.json()

    @staticmethod
    def list(params: Dict, next: str = ""):
        client = Client()
        url = "https://api.ledgerx.com/trading/trades/global"
        default_params = dict(
            status_type=201, limit=50, min_size=100, mine=False, asset="CBTC"
        )
        headers = gen_headers()
        res = client.get(url, headers, params)
        data = res.json()
        return data
