# https://exercism.io/my/solutions/6f3b13fcecf64674acca3c47c621f5f2


def sum_of_multiples(limit, multiples):
    m = set()
    i = 1
    i_multiples = [i * n for n in multiples if n != 0 and i * n < limit]
    while i_multiples:
        m.update(i_multiples)
        i += 1
        i_multiples = [i * n for n in multiples if n != 0 and i * n < limit]
    return sum(m)
