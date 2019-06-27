def primes(limit):
    m = [0] * (limit + 1)
    for n in range(2, limit):
        if m[n] == 0:
            multiple = 2 * n
            while multiple <= limit:
                m[multiple] = n
                multiple += n
    return [i for i, n in enumerate(m) if n == 0 and i >= 2]
