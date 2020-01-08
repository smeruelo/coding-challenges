# Problem: One Away
# There are three types of edits that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# O(n)
def is_one_away_1(s1, s2):

    # O(n)
    def check_one_replacement(sa, sb):
        difference_found = False
        for i in range(len(sa)):
            if sa[i] != sb[i]:
                if difference_found:
                    return False
                else:
                    difference_found = True
        return True

    # O(n)
    def check_one_insertion(sa, sb):
        difference_found = False
        ia = ib = 0
        while ia in range(len(sa)):
            if sa[ia] != sb[ib]:
                if difference_found:
                    return False
                else:
                    difference_found = True
            else:
                ia += 1
            ib += 1
        return True

    if len(s1) - len(s2) == 0:
        return check_one_replacement(s1, s2)
    elif len(s1) - len(s2) == 1:
        return check_one_insertion(s2, s1)
    elif len(s1) - len(s2) == -1:
        return check_one_insertion(s1, s2)
    else:
        return False


# O(n)
def is_one_away_2(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i1 = i2 = 0
    difference_found = False
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if difference_found:
                return False
            difference_found = True
            if len(s1) >= len(s2):
                i1 += 1
            if len(s2) >= len(s1):
                i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True
