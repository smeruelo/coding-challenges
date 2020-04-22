# https://exercism.io/my/solutions/96ac04438bcd4b90a89142a4198ce59f

from math import log


def to_decimal(input_base, digits):
    return sum(digit * (input_base ** power) for power, digit in enumerate(reversed(digits)))


def from_decimal(decimal, output_base):
    output_digits = []
    while decimal > 0:
        output_digits.append(decimal % output_base)
        decimal //= output_base
    return list(reversed(output_digits)) if output_digits else [0]


def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError("Invalid base")
    if any(map(lambda d: True if d < 0 or d >= input_base else False, digits)):
        raise ValueError("Invalid digits")

    return from_decimal(to_decimal(input_base, digits), output_base)
