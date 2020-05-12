# https://exercism.io/my/solutions/b32e89e49bd945799225bb294a842ef6

from collections import Counter
from itertools import permutations


DIGITS = set(range(10))


def evaluate(carry, addends, result, trans):
    """Calculates the value of a 1-digit sum for a given translation table.
    If it matches the expected result, it returns the carry and the translation table used."""

    v1 = trans[result]
    v2 = carry + sum(occurrences * trans[letter] for letter, occurrences in addends.items())
    if v1 == v2 % 10:
        return (v2 // 10, trans)
    return None


def possibilities(carry, addends, result, trans):
    """Calculates all the possible translation table for a 1-digit sum"""

    unused_digits = DIGITS - set(trans.values())
    new_letters = tuple(letter for letter in (set(addends) | {result}) if letter not in trans)
    combo_size = len(new_letters) if new_letters != () else 0
    combos = list(permutations(unused_digits, combo_size))
    def f(combo):
        new_trans = dict(zip(new_letters, combo))
        new_trans.update(trans)
        return evaluate(carry, addends, result, new_trans)
    return list(filter(bool, map(f, combos)))


def column(i, nums, result):
    return (Counter(n[i] for n in nums if len(n) > i), result[i])


def solve(puzzle):
    whole_result = puzzle.split('==')[1].strip()[::-1]
    whole_addends = list(map(lambda s: s.strip()[::-1], puzzle.split('==')[0].split('+')))
    max_length = max(map(len, whole_addends))
    if max_length > len(whole_result):
        return None

    def rec(i, carry, trans):
        if i >= max_length:
            if carry == 0 and i >= len(whole_result):
                return [trans]
            elif carry != 0 and i < len(whole_result):
                carry_unit = carry % 10
                carry_letter = whole_result[i]
                if (carry_letter in trans and trans[carry_letter] != carry_unit) or \
                   (carry_letter not in trans and carry_unit in trans.values()):
                    return []
                if carry_letter not in trans:
                    trans[carry_letter] = carry_unit
                return rec(i+1, carry // 10, trans)
            return []

        solutions = []
        addends, result = column(i, whole_addends, whole_result)
        for next_carry, next_trans in possibilities(carry, addends, result, trans):
            solutions.extend(rec(i+1, next_carry, next_trans))
        return solutions

    result = rec(0, 0, dict())
    return None if len(result) != 1 else result[0]
