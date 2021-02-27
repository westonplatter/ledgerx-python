from typing import Dict, List, Any
from ledgerx import API_BASE, LEGACY_API_BASE
import ledgerx


def gen_headers(include_api_key: bool = False) -> Dict:
    headers = {
        "Accept": "application/json",
    }
    if include_api_key:
        headers["Authorization"] = f"JWT {ledgerx.api_key}"
    return headers


def gen_url(path: str) -> str:
    return f"{API_BASE}{path}"


def gen_legacy_url(path: str) -> str:
    return f"{LEGACY_API_BASE}{path}"


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
