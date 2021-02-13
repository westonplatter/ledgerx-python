from ledgerx import trades


def test_methods():
    class_methods = dir(trades.Trades)
    assert "next" in class_methods
    assert "list" in class_methods
    assert "list_all" in class_methods
