import random as rand


def random(a, b) -> int:
    return rand.randint(a, b)


def absolute_value(num) -> int:
    if num < 0:
        num = 0 - num

    return num
