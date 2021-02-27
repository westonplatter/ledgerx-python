import ledgerx


def test_methods():
    class_methods = dir(ledgerx.Orders)
    assert "cancel_all" in class_methods
    assert "cancel_single" in class_methods
    assert "cancel_replace" in class_methods
    assert "open" in class_methods
