from typing import List, Dict
from ledgerx.client import Client
from ledgerx.util import gen_headers, gen_url
from ledgerx.generic_resource import GenericResource


class Trades:
    default_list_params = dict(
        status_type=201, limit=50, min_size=1, mine=False, asset="CBTC"
    )

    @classmethod
    def next(cls, next_url: str):
        res = Client.get(next_url)
        return res.json()

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        url = gen_url("/trading/trades/global")
        request_params = {**cls.default_list_params, **params}
        res = Client.get(url, request_params)
        data = res.json()
        return data

    @classmethod
    def list_all(cls, params: Dict = {}) -> List[Dict]:
        url = gen_url("/trading/trades/global")
        request_params = {**cls.default_list_params, **params}
        return GenericResource.list_all(url, request_params)
