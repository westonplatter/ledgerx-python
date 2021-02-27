import ledgerx


def test_methods():
    class_methods = dir(ledgerx.Trades)
    assert "next" in class_methods
    assert "list" in class_methods
    assert "list_all" in class_methods
