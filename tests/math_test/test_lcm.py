from maths.utils import *


def test_lcm_with_really_simple_numbers():
    assert lcm(1, 1) == 1


def test_lcm_4_5():
    assert lcm(4, 5) == 20


def test_lcm_5_5():
    assert lcm(5, 5) == 5


def test_lcm_15_37():
    assert lcm(15, 37) == 555


def test_lcm_20_12():
    assert lcm(20, 12) == 60


def test_lcm_300001_285748():
    assert lcm(300001, 285748) == 85724685748

