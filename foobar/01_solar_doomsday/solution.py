from math import sqrt


def max_square(n):
    s = int(sqrt(n))
    return s * s


def as_sum_of_squares(remaining, squares):
    if remaining > 0:
        s = max_square(remaining)
        squares.append(s)
        return as_sum_of_squares(remaining - s, squares)
    else:
        return squares


def solution(area):
    return as_sum_of_squares(area, [])
