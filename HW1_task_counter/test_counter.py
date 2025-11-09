from counter import Counter


def test_0():
    c = Counter()
    assert c.GetCount() == 0


def test_3():
    c = Counter()
    c.Increment()
    c.Increment()
    c.Increment()
    assert c.GetCount() == 3


def test_20():
    c = Counter()
    for i in range(20):
        c.Increment()

    assert c.GetCount() == 20
