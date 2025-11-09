from sortercombiner import SorterCombiner


def test_empty():
    sc = SorterCombiner()    
    assert sc.GetData() == []


def test_init():    
    sc = SorterCombiner([3, 2, 1])    
    assert sc.GetData() == [1, 2, 3]


def test_nothing():
    sc = SorterCombiner()
    sc.LoadNew([])    
    assert sc.GetData() == []


def test_one_load():
    sc = SorterCombiner()
    sc.LoadNew([3, 2, 1])    
    assert sc.GetData() == [1, 2, 3]


def test_two_loads():
    sc = SorterCombiner()
    sc.LoadNew([3, 2, 1])
    sc.LoadNew([5, 4])    
    assert sc.GetData() == [1, 2, 3, 4, 5]



def test_max_load():
    sc = SorterCombiner()
    
    for i in range(0, 20, 3):
        new_load = [x for x in range(i, i + 3)]
        sc.LoadNew(new_load)
    
    result = list([i for i in range(21)])     
    assert sc.GetData() == result
    