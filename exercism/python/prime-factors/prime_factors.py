from math import sqrt


def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def primes():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def prime_factors(number):
    factors = []
    prime_gen = primes()

    f = next(prime_gen)
    while number != 1:
        if number % f == 0:
            factors.append(f)
            number = number // f
        else:
            f = next(prime_gen)

    return factors
