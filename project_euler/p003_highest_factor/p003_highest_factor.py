# https://projecteuler.net/problem=3

import math

def is_prime(n):
    i = int(math.floor(math.sqrt(n)))
    prime = True
    while i > 1 and prime:
        if n % i == 0:
            prime = False
        i -= 1
    return prime

def highest_factor(n):
    i = int(math.floor(math.sqrt(n)))
    factor = n
    while i > 1 and  factor == n:
        if n % i == 0 and is_prime(i):
            factor = i
        i -= 1
    return factor

def main():
    print highest_factor(600851475143)

if __name__ == "__main__":
    main()
