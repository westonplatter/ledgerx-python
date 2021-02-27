from time import sleep
from typing import List, Dict, Callable

from ledgerx import DELAY_SECONDS
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_headers, gen_url, has_next_url


class GenericResource:
    @classmethod
    def next(cls, next_url: str):
        res = HttpClient.get(next_url)
        return res.json()

    @classmethod
    def list(cls, url: str, params: Dict, include_api_key: bool = False):
        res = HttpClient.get(url, params, include_api_key)
        return res.json()

    @classmethod
    def list_all(
        cls,
        url: str,
        params: Dict = {},
        include_api_key: bool = False,
        max_fetches: int = 0,
    ) -> List[Dict]:
        elements = []

        json_data = cls.list(url, params, include_api_key)
        elements.extend(json_data["data"])

        while has_next_url(json_data):
            sleep(DELAY_SECONDS)
            json_data = cls.next(json_data["meta"]["next"])
            elements.extend(json_data["data"])
        return elements

    @classmethod
    def list_all_incremental_return(
        cls,
        url: str,
        params: Dict = {},
        include_api_key: bool = False,
        callback: Callable = None,
        max_fetches: int = 0,
    ) -> None:
        json_data = cls.list(url, params, include_api_key=include_api_key)
        callback(json_data["data"])

        while has_next_url(json_data):
            sleep(DELAY_SECONDS)
            json_data = cls.next(json_data["meta"]["next"])
            callback(json_data["data"])
