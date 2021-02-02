from typing import Dict, List, Any
from ledgerx import API_BASE


def gen_headers() -> Dict:
    return {
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://omni.ledgerx.com",
        "refer": "https://omni.ledgerx.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    }


def gen_url(path: str) -> str:
    return f"{API_BASE}{path}"


def has_next_url(response_data: Dict) -> bool:
    if "meta" in response_data:
        if "next" in response_data["meta"]:
            if response_data["meta"]["next"] != None:
                return True


def unique_values_from_key(elements: List[Dict], key: str) -> List[Any]:
    values = []
    for el in elements:
        values.append(el[key])
    return list(set(values))
