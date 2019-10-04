from maths import *


def test_hcf_with_really_simple_factors():
    assert hcf(1, 1) == 1


def test_hcf_with_equal_factors():
    assert hcf(4, 4) == 4
    assert hcf(5, 5) == 5


def test_hcf_with_factor_2():
    assert hcf(4, 2) == 2


def test_hcf_substution():
    assert hcf(4, 2) == hcf(2, 4)


def test_hcf_with_factor_of_3():
    assert hcf(9, 12) == 3
