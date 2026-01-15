from swap import swap
def test_swap_integers():
    a, b = swap(5, 10)
    assert a == 10
    assert b == 5
def test_swap_same():
    a, b = swap(5, 5)
    assert a == 5
    assert b == 5