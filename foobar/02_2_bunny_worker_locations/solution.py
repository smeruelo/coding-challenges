def sum_of_n_first_naturals(n):
    return (n * (n + 1)) / 2


def solution(x, y):
    return str(sum_of_n_first_naturals(x + y - 1) - y + 1)
