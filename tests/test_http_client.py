from ledgerx.http_client import HttpClient


def test_methods():
    class_methods = dir(HttpClient)
    assert 'get' in class_methods
    assert 'post' in class_methods