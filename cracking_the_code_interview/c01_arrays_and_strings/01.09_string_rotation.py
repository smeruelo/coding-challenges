# Problem: String Rotation
# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a
# rotation of s1 using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of"erbottlewat").


def isSubstring(s1, s2):
    return s2 in s1


def isRotation(s1, s2):
    return len(s1) == len(s2) and isSubstring(s1 + s1, s2)
