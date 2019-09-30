import random as rand
from colorprint import ColorPrint


def random(a, b) -> int:
    return rand.randint(a, b)


def absolute_value(num) -> int:
    if num < 0:
        num = ~num

    return num


class Fraction(object):
    def __init__(self, numerator: int, denomerator: int):
        self.numerator = numerator
        self.denomerator = denomerator

    def display(self):
        print(self.__str__())

    def decimal(self, as_int: bool = None, round_to: int = None):
        if round_to is not None:
            return round(self.numerator/self.denomerator, ndigits=round_to)
        elif as_int:
            return int(round(self.numerator / self.denomerator, ndigits=0))
        else:
            return self.numerator / self.denomerator

    def __str__(self):
        return f"{self.numerator}/{self.denomerator}"

    def __iadd__(self, other):
        if type(other) == int:
            self.numerator += (self.denomerator * other)
        elif type(other) == Fraction:
            if other.denomerator != self.denomerator:
                new_self_numerator = self.numerator * other.denomerator
                other.numerator *= self.denomerator
                self.numerator = new_self_numerator
                self.denomerator = other.denomerator = self.denomerator * other.denomerator
                self.numerator += other.numerator
            else:
                self.numerator += other.numerator

        return self

    def __isub__(self, other):
        if type(other) == int:
            self.numerator -= (self.denomerator * other)
        elif type(other) == Fraction:
            if other.denomerator != self.denomerator:
                new_self_numerator = self.numerator * other.denomerator
                other.numerator *= self.denomerator
                self.numerator = new_self_numerator
                self.denomerator = other.denomerator = self.denomerator * other.denomerator
                self.numerator -= other.numerator
            else:
                self.numerator -= other.numerator

        return self

    def __imul__(self, other):
        if type(other) == int:
            self.numerator *= other
        elif type(other) == Fraction:
            self.numerator *= other.numerator
            self.denomerator *= other.denomerator

        return self

    def __itruediv__(self, other):
        if type(other) == int:
            self.numerator *= Fraction(1, other)
        elif type(other) == Fraction:
            self.numerator *= other.denomerator
            self.denomerator *= other.numerator

        return self

    def __getitem__(self, item):
        if item == 'numerator':
            return self.numerator
        elif item == 'denomerator':
            return self.denomerator
        else:
            ColorPrint.error_print("The given kay is non-existing in a fraction")

    def __setitem__(self, key, value):
        if key == 'numerator':
            self.numerator = value
        elif key == 'denomerator':
            self.denomerator = value
        else:
            ColorPrint.error_print("The given kay is non-existing in a fraction")

    # def separate(self):
    #     return self.numerator, self.denomerator
