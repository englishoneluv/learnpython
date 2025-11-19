from filter import Filter
import time


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

def test_speed():
    start = time.perf_counter()

    f = Filter([i for i in range(500000)])
    container = [i for i in range(0, 500000, 100)]
    after_filtering = f.Apply(container)

    duration = time.perf_counter() - start
    assert duration < 1, f"Duration: {duration:.4f} seconds > 1 sec"