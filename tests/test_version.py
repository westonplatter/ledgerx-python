from ledgerx import version


def test_version():
    assert version.VERSION is not None
