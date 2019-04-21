# https://exercism.io/my/solutions/5a6b231b50ac4f6ab8f3391f87a62638


def is_palindrome(n):
    return int(str(n)[::-1]) == n


def palindrome_and_factors(max_factor, min_factor, func):
    if max_factor < min_factor:
        raise ValueError('Invalid range')

    f = []
    v = None
    for f1 in range(min_factor, max_factor + 1):
        for f2 in range(f1, max_factor + 1):
            product = f1 * f2
            if product == v:
                f.append((f1, f2))
            elif (v is None or product == func(v, product)) and is_palindrome(product):
                v = product
                f = [(f1, f2)]
    if v:
        return v, set(f)
    return None, []


def largest_palindrome(max_factor, min_factor):
    return palindrome_and_factors(max_factor, min_factor, max)


def smallest_palindrome(max_factor, min_factor):
    return palindrome_and_factors(max_factor, min_factor, min)
