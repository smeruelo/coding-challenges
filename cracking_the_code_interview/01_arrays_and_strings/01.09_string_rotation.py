def isSubstring(s1, s2):
    return s2 in s1


def isRotation(s1, s2):
    return len(s1) == len(s2) and isSubstring(s1 + s1, s2)
