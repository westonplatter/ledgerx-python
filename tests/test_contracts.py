import ledgerx


def test_methods():
    class_methods = dir(ledgerx.Contracts)
    assert "next" in class_methods
    assert "list" in class_methods
    assert "list_all" in class_methods
    assert "list_all_expiration_dates" in class_methods
