def is_palindrome(n):
    return int(str(n)[::-1]) == n


def palindromes(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError('Invalid range')

    p = dict()
    for f1 in range(min_factor, max_factor + 1):
        for f2 in range(f1, max_factor + 1):
            product = f1 * f2
            if product in p:
                p[product].add((f1, f2))
            elif is_palindrome(product):
                p[product] = set([(f1, f2)])
    return p


def largest_palindrome(max_factor, min_factor):
    p = palindromes(max_factor, min_factor)
    if p:
        return max(p), p[max(p)]
    return None, []


def smallest_palindrome(max_factor, min_factor):
    p = palindromes(max_factor, min_factor)
    if p:
        return min(p), p[min(p)]
    return None, []
