# Problem: URLify
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"


# O(n)
def urlify(s, n):
    url = list(s)

    spaces = 0
    for i in range(n):
        if url[i] == ' ':
            spaces += 1

    j = n - 1
    i = j + spaces * 2
    while i >= 0:
        if url[j] == ' ':
            url[i] = '0'
            url[i-1] = '2'
            url[i-2] = '%'
            i -= 3
        else:
            url[i] = url[j]
            i -= 1
        j -= 1
    return ''.join(url)
