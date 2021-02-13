from time import sleep
from typing import List, Dict, Callable
import pandas as pd

from ledgerx import DELAY_SECONDS
from ledgerx.http_client import HttpClient
from ledgerx.util import gen_headers, gen_url, has_next_url


class GenericResource:
    @classmethod
    def next(cls, next_url: str):
        res = HttpClient.get(next_url)
        return res.json()

    @classmethod
    def list(cls, url: str, params: Dict):
        res = HttpClient.get(url, params)
        return res.json()

    @classmethod
    def list_all(cls, url: str, params: Dict = {}, max_fetches: int = 0) -> List[Dict]:
        elements = []

        json_data = cls.list(url, params)
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
        callback: Callable = None,
        max_fetches: int = 0,
    ) -> None:
        json_data = cls.list(url, params)
        callback(json_data["data"])

        while has_next_url(json_data):
            sleep(DELAY_SECONDS)
            json_data = cls.next(json_data["meta"]["next"])
            callback(json_data["data"])
