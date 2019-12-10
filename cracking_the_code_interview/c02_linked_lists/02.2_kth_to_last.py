#! /usr/bin/python3
from immutable_singly_linked_list import ISinglyLinkedList


# O(n)
# Recursive, it takes extra O(n) space (n simultaneous recursive calls)
def kth_to_last_rec(k, lst):
    def aux(rest):
        if rest.is_nil():
            return (1, None)
        else:
            count, found = aux(rest.tail)
            if count == k:
                return (count + 1, rest.head)
            return (count + 1, found)

    _, kth = aux(lst)
    if not kth is None:
        return kth
    else:
        raise Exception


# O(n)
# Iterative naive
def kth_to_last_it_1(k, lst):
    def length(lst):
        count = 0
        current = lst
        while not current.is_nil():
            count += 1
            current = current.tail
        return count

    n = length(lst) - k
    if n < 0:
        raise Exception

    count = 0
    current = lst
    while count < n:
        count += 1
        current = current.tail
    return current.head


# O(n)
# Iterative, 2 pointers separated k positions
def kth_to_last_it_2(k, lst):
    diff = 0
    p1 = lst
    while diff < k and not p1.is_nil():
        diff += 1
        p1 = p1.tail

    if p1.is_nil() and diff < k:
        raise Exception

    p2 = lst
    while not p1.is_nil():
        p1 = p1.tail
        p2 = p2.tail
    return p2.head


if __name__ == '__main__':
    l = ISinglyLinkedList().push(0).push(7).push(3).push(2).push(7).push(1).push(0)
    print(l)
    for i in range(1, 10):
        print(i, kth_to_last_rec(i, l))
        print(i, kth_to_last_it_1(i, l))
        print(i, kth_to_last_it_2(i, l))

