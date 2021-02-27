import requests
from typing import Dict

import ledgerx
from ledgerx.util import gen_headers, gen_url


class HttpClient:
    # TODO(weston) - handle rate limiting, https://docs.ledgerx.com/reference#rate-limits

    @staticmethod
    def get(
        url: str, params: Dict = {}, include_api_key: bool = False
    ) -> requests.Response:
        """Excute http get request

        Args:
            url (str): [description]
            params (Dict, optional): [description]. Defaults to {}.
            include_api_key (bool, optional): [description]. Defaults to False.

        Returns:
            requests.Response: [description]
        """
        headers = gen_headers(include_api_key)
        res = requests.get(url, headers=headers, params=params)
        return res

    @staticmethod
    def post(
        url: str, data: Dict = {}, include_api_key: bool = False
    ) -> requests.Response:
        """Execute http post request

        Args:
            url (str): [description]
            data (Dict, optional): [description]. Defaults to {}.
            include_api_key (bool, optional): [description]. Defaults to False.

        Returns:
            requests.Response: [description]
        """
        headers = gen_headers(include_api_key)
        res = requests.post(url, headers=headers, json=data)
        return res

    @staticmethod
    def delete(
        url: str, params: Dict = {}, include_api_key: bool = False
    ) -> requests.Response:
        """Execute http delete request

        Args:
            url (str): [description]
            params (Dict, optional): [description]. Defaults to {}.
            include_api_key (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        headers = gen_headers(include_api_key)
        res = requests.delete(url, params=params, headers=headers)
        return res
