from maths import *


def test_prime_factors_of_1():
    assert prime_factors(1) == [1]


def test_prime_factors_of_2():
    assert prime_factors(2) == [1, 2]


def test_prime_factors_of_5():
    assert prime_factors(5) == [1, 5]


def test_prime_factors_of_24():
    assert prime_factors(24) == [1, 2, 2, 2, 3]


def test_prime_factors_of_81():
    assert prime_factors(81) == [1, 3, 3, 3, 3]
