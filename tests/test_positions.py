import ledgerx


def test_methods():
    class_methods = dir(ledgerx.Positions)
    assert "list" in class_methods
    assert "list_trades" in class_methods
