from alarm import Alarm


def test_early():
    a = Alarm(5)
    time = 4
    assert a.isEarly(time) == True
    assert a.isTooLate(time) == False


def test_on_time():
    a = Alarm(5)
    time = 5
    assert a.isEarly(time) == False
    assert a.isTooLate(time) == False


def test_zero():
    a = Alarm(5)
    time = 6
    assert a.isEarly(time) == False
    assert a.isTooLate(time) == True
