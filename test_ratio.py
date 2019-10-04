from maths import Ratio


def test_ratio_equal_overloading_method_with_the_same_terms():
    assert Ratio(2, 3) == Ratio(2, 3)


def test_ratio_equal_overloading_method_without_the_same_terms():
    assert not(Ratio(4, 6) == Ratio(5, 6))


def test_ratio_simplify_method_with_simplifiable_ratios():
    assert Ratio(3, 9).simplify() == Ratio(1, 3)


def test_ratio_simplify_method_with_non_simplifiable_ratios():
    assert Ratio(5, 7).simplify() == Ratio(5, 7)


def test_ratio_division_with_dividable_numbers():
    assert Ratio(3, 9) / 3 == Ratio(1, 3)
