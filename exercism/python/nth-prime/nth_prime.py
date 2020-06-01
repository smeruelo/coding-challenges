# https://exercism.io/my/solutions/9483c47c57bb449cb6395acec6256dae

from math import sqrt


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def prime(nth):
    if nth < 1:
        raise ValueError("Wrong argument.")
    if nth == 1:
        return 2

    count = 1
    n = 1
    while count < nth:
        n += 2
        if is_prime(n):
            count += 1
    return n
