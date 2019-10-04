class Ratio(object):
    def __init__(self, first_term: int, second_term: int, first_term_name='of 1st term', second_term_name='of 2nd term'):
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

    def __ne__(self, other):
        return self.first_term / self.second_term != other.first_term / other.second_term

    def __gt__(self, other):
        return self.first_term / self.second_term > other.first_term / other.second_term

    def __lt__(self, other):
        return self.first_term / self.second_term < other.first_term / other.second_term

    def __ge__(self, other):
        return self.first_term / self.second_term >= other.first_term / other.second_term

    def __le__(self, other):
        return self.first_term / self.second_term <= other.first_term / other.second_term
