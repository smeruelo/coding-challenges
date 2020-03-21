# https://exercism.io/my/solutions/6b7e0de8f73a4aba88d7387866d37d5b


def append(lst1, lst2):
    len1, len2 = length(lst1), length(lst2)
    l = [None] * (len1 + len2)
    for i in range(len1):
        l[i] = lst1[i]
    for i in range(len2):
        l[len1 + i] = lst2[i]
    return l


def concat(lsts):
    if length(lsts) == 0:
        return []
    l = lsts[0]
    for i in range(1, len(lsts)):
        l = append(l, lsts[i])
    return l


def filter(function, lst):
    l = []
    for item in lst:
        if function(item):
            l = append(l, [item])
    return l


def length(lst):
    i = 0
    while True:
        try:
            lst[i]
            i += 1
        except IndexError:
            return i


def map(function, lst):
    l = [None] * length(lst)
    for i in range(length(l)):
        l[i] = function(lst[i])
    return l


def foldl(function, lst, initial):
    accum = initial
    for item in lst:
        accum = function(accum, item)
    return accum


def foldr(function, lst, initial):
    accum = initial
    for i in range(length(lst)-1, -1, -1):
        accum = function(lst[i], accum)
    return accum


def reverse(lst):
    l = []
    for i in range(length(lst)-1, -1, -1):
        l = append(l, [lst[i]])
    return l
        
