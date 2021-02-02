from time import sleep
from typing import List, Dict
import pandas as pd

from ledgerx import DELAY_SECONDS
from ledgerx.client import Client
from ledgerx.util import gen_headers, gen_url, has_next_url


class GenericResource:
    @classmethod
    def next(cls, next_url: str):
        res = Client.get(next_url)
        return res.json()

    @classmethod
    def list(cls, url: str, params: Dict):
        res = Client.get(url, params)
        return res.json()

    @classmethod
    def list_all(cls, url: str, params: Dict = {}, max_fetches=0) -> List[Dict]:
        elements = []

        json_data = cls.list(url, params)
        elements.extend(json_data["data"])

        while has_next_url(json_data):
            sleep(DELAY_SECONDS)
            json_data = cls.next(json_data["meta"]["next"])
            elements.extend(json_data["data"])
            df = pd.DataFrame.from_dict(elements)
            df.to_csv("all_trades.csv")
            print(f"data = {len(elements)}")

        return elements
