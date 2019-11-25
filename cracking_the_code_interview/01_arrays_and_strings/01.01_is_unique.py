from collections import defaultdict


# O(n)
def is_unique_1(s):
    appeared = defaultdict(bool)
    for char in s:
        if appeared[char]:
            return False
        appeared[char] = True
    return True


# No additional data structures
# O(n * n)
def is_unique_2(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


# No additional data structures
# O(n log n)
# Let's suppose we have a list instead of string
# (because strings are immutable in python)
def is_unique_3(sl):
    sl.sort()
    for i in range(1, len(sl)):
        if sl[i] == sl[i - 1]:
            return False
    return True
