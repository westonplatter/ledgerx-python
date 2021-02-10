from typing import List, Dict
from ledgerx.http_client import HttpClient
from ledgerx.generic_resource import GenericResource
from ledgerx.util import gen_headers, gen_url, has_next_url, unique_values_from_key


class Contracts:
    default_list_params = dict(active=True)

    @classmethod
    def next(cls, next_url: str) -> Dict:
        res = HttpClient.get(next_url)
        return res.json()

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        res = HttpClient.get(url, qps)
        return res.json()

    @classmethod
    def list_all(cls, params: Dict = {}) -> List[str]:
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        return GenericResource.list_all(url, qps)

    @classmethod
    def list_all_expiration_dates(cls, params: Dict = {}) -> List[str]:
        contracts = cls.list_all(params)
        exp_dates = unique_values_from_key(contracts, "date_expires")
        return sorted(exp_dates)
