from collections import defaultdict


# O(n)
def is_palindrome_permutation(s):
    count = Counter(s.lower())
    del count[' ']

    # To be able to form a palindrome out of these chars,
    # only 0 or 1 of them can appear an odd number of times
    odds = 0
    for char in count:
        if count[char] % 2 == 1:
            odds += 1
    return odds <= 1
