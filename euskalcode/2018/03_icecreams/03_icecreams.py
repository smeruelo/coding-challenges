#!/usr/bin/python3

import math
import os
import random
import re
import sys

def numeroHelados(cases):
    def aux(wrappers, count):
        if wrappers < required:
            return count
        new = wrappers // required
        return aux(wrappers - (new * required) + new, count + new)

    for case in cases:
        money, price, required = map(int, case.split())
        print(aux(money // price, money // price))


if __name__ == '__main__':
    casos_count = int(input())

    casos = []

    for _ in range(casos_count):
        casos_item = input()
        casos.append(casos_item)

    numeroHelados(casos)
