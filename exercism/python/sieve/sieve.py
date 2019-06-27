# https://exercism.io/my/solutions/71af6b0543e148b9af5c3b8f2af9eda7


def primes(limit):
    m = [0] * (limit + 1)
    primes = []
    for n in range(2, limit + 1):
        if m[n] == 0:
            primes.append(n)
            multiple = 2 * n
            while multiple <= limit:
                m[multiple] = n
                multiple += n
    return primes
