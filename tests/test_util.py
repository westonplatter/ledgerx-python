from ledgerx import util


def test_gen_headers():
    headers = util.gen_headers()
    assert type(headers) == dict


def test_gen_url():
    url = util.gen_url("/myurl")
    assert url == "https://api.ledgerx.com/myurl"
