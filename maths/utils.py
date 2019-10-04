import random as rand


def random(a, b) -> int:
    return rand.randint(a, b)


def absolute_value(num) -> int:
    if num < 0:
        num = ~num

    return num


def hcf(factor_1: int, factor_2: int):
    fac_1_prime_factors = prime_factors(factor_1)
    fac_2_prime_factors = prime_factors(factor_2)
    result = 1

    for i in range(len(fac_1_prime_factors) - 1, 0, -1):
        for x in range(len(fac_2_prime_factors) - 1, 0, -1):
            if fac_1_prime_factors[i] == fac_2_prime_factors[x]:
                result = fac_1_prime_factors[i]
                break

    return result


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
