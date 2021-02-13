from typing import List, Dict, Callable
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_headers, gen_url
from ledgerx.generic_resource import GenericResource


class Trades:
    default_list_params = dict(
        status_type=201, limit=50, min_size=1, mine=False, asset="CBTC"
    )

    @classmethod
    def next(cls, next_url: str):
        res = HttpClient.get(next_url)
        return res.json()

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        url = gen_url("/trading/trades/global")
        request_params = {**cls.default_list_params, **params}
        res = HttpClient.get(url, request_params)
        data = res.json()
        return data

    @classmethod
    def list_all(cls, params: Dict = {}) -> List[Dict]:
        url = gen_url("/trading/trades/global")
        request_params = {**cls.default_list_params, **params}
        return GenericResource.list_all(url, request_params)

    @classmethod
    def list_all_incremental_return(cls, params: Dict = {}, callback: Callable = None):
        url = gen_url("/trading/trades/global")
        request_params = {**cls.default_list_params, **params}
        return GenericResource.list_all_incremental_return(url, params, callback)
