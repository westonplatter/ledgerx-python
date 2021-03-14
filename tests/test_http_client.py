import pytest
import requests_mock
import requests

from ledgerx.http_client import HttpClient


def test_methods():
    class_methods = dir(HttpClient)
    assert "get" in class_methods
    assert "post" in class_methods
    assert "delete" in class_methods


def test_get_raise_status():
    uri = "https://google.com/"
    with requests_mock.Mocker() as m:
        m.register_uri("GET", uri, status_code=500)
        with pytest.raises(requests.exceptions.HTTPError):
            res = HttpClient.get(uri)
            assert res.status_code == 500


def test_put_raise_status():
    uri = "https://google.com/"
    with requests_mock.Mocker() as m:
        m.register_uri("POST", uri, status_code=403)
        with pytest.raises(requests.exceptions.HTTPError):
            res = HttpClient.post(uri)
            assert res.status_code == 403


def test_delete_raise_status():
    uri = "https://google.com/"
    with requests_mock.Mocker() as m:
        m.register_uri("DELETE", uri, status_code=400)
        with pytest.raises(requests.exceptions.HTTPError):
            res = HttpClient.delete(uri)
            assert res.status_code == 400
