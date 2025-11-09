from filter import Filter


def test_empty():
    f = Filter([])
    container = [1, 2, 3, 4, 5]
    after_filtering = f.Apply(container) 
    assert after_filtering == [1, 2, 3, 4, 5]

def test_nothing():
    f = Filter([42, 57, -1])
    container = [1, 2, 3, 4, 5]
    after_filtering = f.Apply(container) 
    assert after_filtering == [1, 2, 3, 4, 5]

def test_some():
    f = Filter([1, 3])
    container = [1, 2, 3, 4, 5]
    after_filtering = f.Apply(container) 
    assert after_filtering == [2, 4, 5]

def test_all():
    f = Filter([1, 2, 3, 4, 5])
    container = [1, 2, 3, 4, 5]
    after_filtering = f.Apply(container) 
    assert after_filtering == []