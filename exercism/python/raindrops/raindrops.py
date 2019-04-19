#!/usr/bin/python3
# https://exercism.io/my/solutions/e3c1cfe830fe4c3498baca47408220c3


def raindrops(number):
    pling = 'Pling' if number % 3 == 0 else ''
    plang = 'Plang' if number % 5 == 0 else ''
    plong = 'Plong' if number % 7 == 0 else ''
    output = pling + plang + plong
    return output if output else str(number)
