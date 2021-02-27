from typing import List, Dict
from ledgerx.http_client import HttpClient
from ledgerx.generic_resource import GenericResource
from ledgerx.util import gen_headers, gen_url, has_next_url, unique_values_from_key


class Contracts:
    default_list_params = dict(active=True)
    default_list_traded = dict(derivative_type=None, asset=None)

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        """List contracts

        Args:
            params (Dict, optional): [description]. Defaults to {}.

        Returns:
            List[Dict]: [description]
        """
        include_api_key = False
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        res = HttpClient.get(url, qps, include_api_key)
        return res.json()

    @classmethod
    def list_traded(cls, params: Dict = {}) -> List[Dict]:
        """List traded contracts

        Args:
            params (Dict, optional): [description]. Defaults to {}.

        Returns:
            List[Dict]: [description]
        """
        include_api_key = True
        url = gen_url("/trading/contracts/traded")
        qps = {**cls.default_list_traded, **params}
        res = HttpClient.get(url, qps, include_api_key)
        return res.json()

    @classmethod
    def retrieve(cls, contract_id: int) -> Dict:
        """Returns your position for a given contract.

        https://docs.ledgerx.com/reference#retrievecontract

        Args:
            contract_id (int): [description]

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_url(f"/trading/contracts/{contract_id}")
        res = HttpClient.get(url, {}, include_api_key)
        return res.json()

    @classmethod
    def retrieve_position(cls, contract_id: int) -> Dict:
        """Returns contract details for a a single contract ID.

        https://docs.ledgerx.com/reference#positioncontract

        Args:
            contract_id (int): LedgerX contract ID

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_url(f"/trading/contracts/{contract_id}/position")
        res = HttpClient.get(url, {}, include_api_key)
        return res.json()

    ### helper methods specific to this API client

    @classmethod
    def list_all(cls, params: Dict = {}) -> List[str]:
        include_api_key = False
        url = gen_url("/trading/contracts")
        qps = {**cls.default_list_params, **params}
        return GenericResource.list_all(url, qps, include_api_key)

    @classmethod
    def next(cls, next_url: str) -> Dict:
        res = HttpClient.get(next_url)
        return res.json()

    @classmethod
    def list_all_expiration_dates(cls, params: Dict = {}) -> List[str]:
        """List all expiration dates for Listed Contracts

        Args:
            params (Dict, optional): . Defaults to {}.

        Returns:
            List[str]: [description]
        """
        contracts = cls.list_all(params)
        exp_dates = unique_values_from_key(contracts, "date_expires")
        return sorted(exp_dates)
