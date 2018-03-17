# https://projecteuler.net/problem=4

def is_palindrome(n):
    return n == n[::-1]

def largest_palindrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range (i, 99, -1):
            product = i * j
            if is_palindrome(str(product)) and product > largest:
                largest = product
    return largest

print largest_palindrome()
