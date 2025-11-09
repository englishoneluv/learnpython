from sum import Sum

def test_positive():
    assert Sum(5, 1) == 6

def test_negative():
    assert Sum(-1, -3) == -3


def test_zero():
    assert Sum(0, 0) == 0
