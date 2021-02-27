from typing import Dict
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_legacy_url


class Orders:
    default_list_params = dict()

    @classmethod
    def cancel_all(cls) -> Dict:
        """Delete all outstanding orders associated with your MPID (the whole organization)

        https://docs.ledgerx.com/reference#cancel-all

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_legacy_url("/orders")
        res = HttpClient.delete(url, {}, include_api_key)
        return res.json()

    @classmethod
    def cancel_single(cls, mid: str, contract_id: int) -> Dict:
        """Cancel a single resting limit order

        https://docs.ledgerx.com/reference#cancel-single

        Args:
            mid (str): [description]

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_legacy_url(f"/orders/{mid}")
        qps = dict(contract_id=contract_id)
        res = HttpClient.delete(url, qps, include_api_key)
        return res.json()

    @classmethod
    def cancel_replace(cls, mid: str, contract_id: int, price: int, size: int) -> Dict:
        """Atomically swap an existing resting limit order with a new resting limit order. Price, side and size may be changed.

        Rate Limit Notice: This endpoint has a rate limit of 500 requests per 10 seconds.

        https://docs.ledgerx.com/reference#cancel-replace

        Args:
            mid (str): [description]
            contract_id (int): [description]
            price (int): [description]
            size (int): [description]

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_legacy_url(f"/orders/{mid}")
        qps = dict(contract_id=contract_id, price=price, size=size)
        res = HttpClient.post(url, qps, include_api_key)
        return res.json()

    @classmethod
    def open(cls, params: Dict = {}) -> Dict:
        """Get all resting limit orders directly from the exchange

        https://docs.ledgerx.com/reference#open-orders

        Args:
            params (Dict, optional): [description]. Defaults to {}.

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_legacy_url(f"/open-orders")
        res = HttpClient.get(url, {}, include_api_key)
        return res.json()
