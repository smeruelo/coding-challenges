#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range (1, n + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[1:].rjust(width + 1)
        hexadecimal = hex(i)[2:].upper().rjust(width + 1)
        binary = bin(i)[2:].rjust(width + 1)
        print decimal + octal + hexadecimal + binary

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
