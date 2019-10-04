import random as rand
from colorprint import ColorPrint


def random(a, b) -> int:
    return rand.randint(a, b)


def absolute_value(num) -> int:
    if num < 0:
        num = ~num

    return num


def hcf(factor_1, factor_2):
    if factor_1 < factor_2:
        return factor_1
    else:
        return factor_2


def prime_factors(num):
    factors = [1]
    divisor = 2
    n = num

    if n == 1:
        return factors

    while True:
        if n % divisor == 0:
            factors.append(divisor)
            if n == divisor:
                break
            n = n//divisor
        else:
            divisor += 1

    return factors


class Fraction(object):
    def __init__(self, numerator: int, denomerator: int):
        self.numerator = numerator
        self.denomerator = denomerator

    def display(self):
        print(self.__str__())

    def decimal(self, as_int: bool = None, round_to: int = None):
        if round_to is not None:
            return round(self.numerator / self.denomerator, ndigits=round_to)
        elif as_int:
            return int(round(self.numerator / self.denomerator, ndigits=0))
        else:
            return self.numerator / self.denomerator

    def simplify(self):
        simplified = False
        divisor = 1

        while not simplified:
            if divisor > self.denomerator or divisor > self.numerator:
                simplified = True
            elif self.numerator % divisor == 0 and self.denomerator % divisor == 0:
                self.numerator //= divisor
                self.denomerator //= divisor
                divisor += 1
            else:
                divisor += 1

        return self

    def __str__(self):
        return f"{self.numerator}/{self.denomerator}"

    def __add__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            numerator += (denomerator * other)
        elif type(other) == Fraction:
            if other.denomerator != denomerator:
                new_self_numerator = numerator * other.denomerator
                other.numerator *= denomerator
                numerator = new_self_numerator
                denomerator = other.denomerator = denomerator * other.denomerator
                numerator += other.numerator
            else:
                numerator += other.numerator

        return Fraction(numerator, denomerator)

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

    def __sub__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            numerator -= (denomerator * other)
        elif type(other) == Fraction:
            if other.denomerator != denomerator:
                new_self_numerator = numerator * other.denomerator
                other.numerator *= denomerator
                numerator = new_self_numerator
                denomerator = other.denomerator = denomerator * other.denomerator
                numerator -= other.numerator
            else:
                numerator -= other.numerator

        return Fraction(numerator, denomerator)

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

    def __mul__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            numerator *= other
        elif type(other) == Fraction:
            numerator *= other.numerator
            denomerator *= other.denomerator

        return Fraction(numerator, denomerator)

    def __imul__(self, other):
        if type(other) == int:
            self.numerator *= other
        elif type(other) == Fraction:
            self.numerator *= other.numerator
            self.denomerator *= other.denomerator

        return self

    def __truediv__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            return Fraction(1, other)
        elif type(other) == Fraction:
            numerator *= other.denomerator
            denomerator *= other.numerator

            return Fraction(numerator, denomerator)

    def __idiv__(self, other):
        if type(other) == int:
            self.numerator *= Fraction(1, other)
        elif type(other) == Fraction:
            self.numerator *= other.denomerator
            self.denomerator *= other.numerator

        return self

    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() == other
        elif type(other) == Fraction:
            return self.decimal() == other.decimal()

    def __ne__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() != other
        elif type(other) == Fraction:
            return self.decimal() != other.decimal()

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() > other
        elif type(other) == Fraction:
            return self.decimal() > other.decimal()

    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() < other
        elif type(other) == Fraction:
            return self.decimal() < other.decimal()

    def __ge__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() >= other
        elif type(other) == Fraction:
            return self.decimal() >= other.decimal()

    def __le__(self, other):
        if type(other) == int or type(other) == float:
            return self.decimal() <= other
        elif type(other) == Fraction:
            return self.decimal() <= other.decimal()

    def __getitem__(self, item):
        if item == 'numerator':
            return self.numerator
        elif item == 'denomerator':
            return self.denomerator
        else:
            ColorPrint.error_print("The given key doesn't exist in a fraction")

    def __setitem__(self, key, value):
        if key == 'numerator':
            self.numerator = value
        elif key == 'denomerator':
            self.denomerator = value
        else:
            ColorPrint.error_print("The given key doesn't exist in a fraction")


class Ratio(object):
    def __init__(self, first_term, second_term, first_term_name='of 1st term', second_term_name='of 2nd term'):
        self.first_term = first_term
        self.first_term_name = first_term_name
        self.second_term = second_term
        self.second_term_name = second_term_name

    def display(self, non_mathematical_display=False):
        NON_MATHEMATICAL_DISPLAY = \
            f"{self.first_term} {self.first_term_name}" \
                f" per " \
                f"{self.second_term} {self.second_term_name}"
        if non_mathematical_display:
            print(NON_MATHEMATICAL_DISPLAY)
        else:
            print(self.__str__())

    def simplify(self):
        simplified = False
        divisor = 1

        while not simplified:
            if divisor > self.second_term or divisor > self.first_term:
                simplified = True
            elif self.first_term % divisor == 0 and self.second_term % divisor == 0:
                self.first_term //= divisor
                self.second_term //= divisor
                divisor += 1
            else:
                divisor += 1

        return self

    def __decimal(self):
        return self.first_term/self.second_term

    def __str__(self):
        return f"{self.first_term}:{self.second_term}"

    def __imul__(self, other):
        self.first_term *= other
        self.second_term *= other

        return self

    def __mul__(self, other):
        first_term = self.first_term
        second_term = self.second_term

        first_term *= other
        second_term *= other

        return Ratio(first_term, second_term, self.first_term_name, self.second_term_name)

    def __truediv__(self, other):
        first_term = self.first_term
        second_term = self.second_term

        first_term /= other
        second_term /= other

        return Ratio(first_term, second_term, self.first_term_name, self.second_term_name)

    def __idiv__(self, other):
        self.first_term /= other
        self.second_term /= other

        return self

    def __eq__(self, other):
        return self.first_term/self.second_term == other.first_term/other.second_term
