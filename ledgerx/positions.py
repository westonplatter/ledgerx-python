from typing import List, Dict
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_headers, gen_url, has_next_url, unique_values_from_key


class Positions:
    default_list_params = dict()
    # default_list_traded = dict(derivative_type=None, asset=None)

    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        """Returns all your positions.

        https://docs.ledgerx.com/reference#listpositions

        Args:
            params (Dict, optional): [description]. Defaults to {}.

        Returns:
            List[Dict]: [description]
        """
        include_api_key = True
        url = gen_url("/trading/positions")
        qps = {**cls.default_list_params, **params}
        res = HttpClient.get(url, qps, include_api_key)
        return res.json()

    @classmethod
    def list_trades(cls, contract_id: int) -> Dict:
        """Returns a list of your trades for a given position.

        Args:
            contract_id (int): LedgerX contract ID.

        Returns:
            Dict: [description]
        """
        include_api_key = True
        url = gen_url(f"/trading/positions/{contract_id}/trades")
        res = HttpClient.get(url, {}, include_api_key)
        return res.json()

    ### helper methods specific to this API client
