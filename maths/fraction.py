class Fraction(object):
    """
    Fraction
    
    Use this tool to create & calculate with fractions
    
    Parameters:
        Numerator: the numerator of the fraction
    """
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

    def __mul__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            numerator *= other
        elif type(other) == Fraction:
            numerator *= other.numerator
            denomerator *= other.denomerator

        return Fraction(numerator, denomerator)

    def __truediv__(self, other):
        numerator = self.numerator
        denomerator = self.denomerator
        if type(other) == int:
            return Fraction(1, other)
        elif type(other) == Fraction:
            numerator *= other.denomerator
            denomerator *= other.numerator

            return Fraction(numerator, denomerator)

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
