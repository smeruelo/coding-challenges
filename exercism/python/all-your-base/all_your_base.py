from math import log


def to_decimal(input_base, digits):
    decimal = 0
    for power, digit in enumerate(reversed(digits)):
        decimal += digit * (input_base ** power)
    return decimal


def from_decimal(decimal, output_base):
    if decimal == 0:
        return [0]

    max_power = int(log(decimal, output_base))
    output_digits = []
    for power in range(max_power, -1, -1):
        weight = output_base ** power
        output_digits.append(decimal // weight)
        decimal -= (decimal // weight) * weight
    return output_digits


def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError("Invalid base")
    if any(map(lambda d: True if d < 0 or d >= input_base else False, digits)):
        raise ValueError("Invalid digits")

    return from_decimal(to_decimal(input_base, digits), output_base)
