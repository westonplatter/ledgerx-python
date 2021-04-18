import requests
from typing import Dict
from time import sleep
from ledgerx.util import gen_headers
from ledgerx import DELAY_SECONDS

import logging

class HttpClient:
    # TODO(weston) - handle rate limiting, https://docs.ledgerx.com/reference#rate-limits
    RETRY_429_ERRORS = False

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
        delay = DELAY_SECONDS
        headers = gen_headers(include_api_key)
        res = None
        while True:
            res = requests.get(url, headers=headers, params=params)
            logging.debug(f"get {url} {res}")
            if HttpClient.RETRY_429_ERRORS and res.status_code == 429:
                if delay == DELAY_SECONDS:
                    delay += 1
                else:
                    delay *= 2.0
                if delay > 10:
                    delay = 10
                logging.info(f"Got 429, delaying {delay}s before retry of url: {url}")
                sleep(delay)
            else:
                res.raise_for_status()
                break
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
        res.raise_for_status()
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
        res.raise_for_status()
        return res
