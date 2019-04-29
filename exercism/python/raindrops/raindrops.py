#!/usr/bin/python3
# https://exercism.io/my/solutions/e3c1cfe830fe4c3498baca47408220c3


def raindrops(number):
    factors = [3, 5, 7]
    strings = ['Pling', 'Plang', 'Plong']
    outputs = [w if number % f == 0 else '' for f, w in zip(factors, strings)]
    return ''.join(outputs) or str(number)
