# https://exercism.io/my/solutions/27867a1fd02e49b5a4de832109d34149


def prime_factors(number):
    factors = []
    f = 2
    while number != 1:
        if number % f == 0:
            factors.append(f)
            number = number // f
        else:
            f += 1

    return factors
