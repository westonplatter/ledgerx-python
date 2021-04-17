from typing import List, Dict
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_url


class Bitvol:
    @classmethod
    def list(cls, params: Dict = {}) -> List[Dict]:
        """Get bitvol data

        Args:
            params (Dict, optional): [description]. Defaults to {}.

        Returns:
            List[Dict]: bitvol objects
        """
        include_api_key = True
        url = gen_url("/trading/bitvol")
        res = HttpClient.get(url, params, include_api_key)
        return res.json()

    ### Helper methods

    @classmethod
    def list_btc(cls, params: Dict = {}) -> List[Dict]:
        """Fetch BTC bitvol data

        Args:
            params (Dict): [description]

        Returns:
            List[Dict]: [description]
        """
        default_params = {"asset": "BTC", "resolution": "1W"}
        qps = {**default_params, **params}
        return cls.list(qps)

    @classmethod
    def list_eth(cls, params: Dict = {}) -> List[Dict]:
        """Fetch ETH bitvol data

        Args:
            params (Dict): [description]

        Returns:
            List[Dict]: [description]
        """
        default_params = {"asset": "ETH", "resolution": "1W"}
        qps = {**default_params, **params}
        return cls.list(qps)
