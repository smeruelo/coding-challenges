# https://exercism.io/my/solutions/6b7e0de8f73a4aba88d7387866d37d5b


def cons(item, lst):
    return [item, *lst]


def foldl(function, lst, accum):
    if not lst:
        return accum
    car, *cdr = lst
    return foldl(function, cdr, function(accum, car))


def foldr(function, lst, initial):
    if not lst:
        return initial
    car, *cdr = lst
    return function(car, foldr(function, cdr, initial))


def append(lst1, lst2):
    return foldr(cons, lst1, lst2)


def concat(lsts):
    return foldl(append, lsts, [])


def filter(function, lst):
    return foldr(lambda car, accum: cons(car, accum) if function(car) else accum, lst, [])


def length(lst):
    return foldl(lambda car, _: car + 1, lst, 0)


def map(function, lst):
    return foldr(lambda car, accum: cons(function(car), accum), lst, [])


def reverse(lst):
    return foldl(lambda accum, car: cons(car, accum), lst, [])
