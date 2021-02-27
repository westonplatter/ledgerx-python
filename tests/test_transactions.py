import ledgerx


def test_methods():
    class_methods = dir(ledgerx.Transactions)
    assert "list" in class_methods
