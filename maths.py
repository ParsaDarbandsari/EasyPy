import random as rand
from colorprint import ColorPrint


def random(a, b) -> int:
    return rand.randint(a, b)


def absolute_value(num) -> int:
    if num < 0:
        num = ~num

    return num


class Fraction(object):
    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        self.fraction = {'numerator': self.numerator, 'denominator': self.denomerator}

    def display(self):
        print(self.__str__())

    def __str__(self):
        return f"{self.fraction['numerator']}/{self.fraction['denominator']}"

    def __imul__(self, other):
        if type(other) == int:
            self.fraction['numerator'] *= other
        elif type(other) == Fraction:
            self.fraction['numerator'] *= other['numerator']
            self.fraction['denominator'] *= other['denominator']

        return self

    def __itruediv__(self, other):
        if type(other) == int:
            self.fraction['numerator'] *= Fraction(1, other)
        elif type(other) == Fraction:
            self.fraction['numerator'] *= other['denominator']
            self.fraction['denominator'] *= other['numerator']

        return self

    def __getitem__(self, item):
        try:
            return self.fraction[item]
        except KeyError:
            ColorPrint.error_print("The given kay is non-existing in a fraction")
