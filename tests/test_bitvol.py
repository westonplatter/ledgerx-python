import ledgerx
import requests_mock


def test_methods():
    class_methods = dir(ledgerx.Bitvol)
    assert "list" in class_methods
    assert "list_btc" in class_methods
    assert "list_eth" in class_methods


def test_list_btc():
    with requests_mock.Mocker() as mock:
        btc_vols = [
            {"time": "2021-04-17T17:36:44.012066Z", "value": 75.35},
            {"time": "2021-04-17T17:30:00Z", "value": 75.48},
            {"time": "2021-04-17T17:20:00Z", "value": 75.5},
        ]
        mock.get(
            "https://api.ledgerx.com/trading/bitvol?asset=BTC&resolution=1D",
            json={"data": btc_vols},
        )
        data = ledgerx.Bitvol.list_btc({"resolution": "1D"})
        assert len(data["data"]) == 3


def test_list_eth():
    with requests_mock.Mocker() as mock:
        eth_vols = [
            {"time": "2021-04-17T17:20:00Z", "value": 82.6},
            {"time": "2021-04-17T17:30:00Z", "value": 84.4},
            {"time": "2021-04-17T17:40:00Z", "value": 84.46},
            {"time": "2021-04-17T17:42:12.122520Z", "value": 84.42},
        ]
        mock.get(
            "https://api.ledgerx.com/trading/bitvol?asset=ETH&resolution=1D",
            json={"data": eth_vols},
        )
        data = ledgerx.Bitvol.list_eth({"resolution": "1D"})
        assert len(data["data"]) == 4
