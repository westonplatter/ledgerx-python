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
    def retrieve(cls, contract_id: int) -> Dict:
        include_api_key = True
        url = gen_url(f"/trading/contracts/{contract_id}")
        res = HttpClient.get(url, {}, include_api_key)
        return res.json()

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        include_api_key = False
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        res = HttpClient.get(url, qps, include_api_key)
        return res.json()

    @classmethod
    def list_traded(cls, params: Dict = {}) -> List[Dict]:
        include_api_key = True
        url = gen_url("/trading/contracts/traded")
        qps = {**cls.default_list_params, **params}
        res = HttpClient.get(url, qps, include_api_key)
        return res.json()

    @classmethod
    def list_all(cls, params: Dict = {}) -> List[str]:
        include_api_key = False
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        return GenericResource.list_all(url, qps, include_api_key)

    @classmethod
    def list_all_expiration_dates(cls, params: Dict = {}) -> List[str]:
        contracts = cls.list_all(params)
        exp_dates = unique_values_from_key(contracts, "date_expires")
        return sorted(exp_dates)
