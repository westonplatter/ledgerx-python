from time import sleep
from typing import List, Dict, Callable

from ledgerx import DELAY_SECONDS
from ledgerx.http_client import HttpClient
from ledgerx.util import has_next_url


class GenericResource:
    @classmethod
    def next(cls, next_url: str, params: Dict, include_api_key: bool = False):
        res = HttpClient.get(next_url, params, include_api_key)
        json_data = res.json()
        logging.debug(f"next {next_url} got {res} {json_data}")
        return json_data

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
        delay: float = DELAY_SECONDS,
    ) -> List[Dict]:
        elements = []

        json_data = cls.list(url, params, include_api_key)
        elements.extend(json_data["data"])
        fetches = 1

        while has_next_url(json_data):
            if max_fetches > 0 and fetches >= max_fetches:
                break
            sleep(delay)
            json_data = cls.next(json_data["meta"]["next"], params, include_api_key)
            elements.extend(json_data["data"])
            fetches += 1
        return elements

    @classmethod
    def list_all_incremental_return(
        cls,
        url: str,
        params: Dict = {},
        include_api_key: bool = False,
        callback: Callable = None,
        max_fetches: int = 0,
        delay: float = DELAY_SECONDS,
    ) -> None:
        json_data = cls.list(url, params, include_api_key=include_api_key)
        callback(json_data["data"])
        fetches = 1

        while has_next_url(json_data):
            if max_fetches > 0 and fetches >= max_fetches:
                break
            sleep(delay)
            json_data = cls.next(json_data["meta"]["next"], params, include_api_key)
            callback(json_data["data"])
            fetches += 1
