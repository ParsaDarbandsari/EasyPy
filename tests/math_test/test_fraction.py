from maths.fraction import Fraction


def test_simplify_fraction_eight_twelveth():
    assert Fraction(8, 12).simplify() == Fraction(2, 3)
    assert Fraction(27, 81).simplify() == Fraction(1, 3)
