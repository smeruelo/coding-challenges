#! /usr/bin/python3
from mutable_singly_linked_list import MSinglyLinkedList


# O(n)
# It takes extra O(n) space, it stores nodes in a dictionary
def first_node_in_loop_1(lst):
    nodes = dict()
    current = lst.head
    while not current.is_last():
        if current in nodes:
            return current
        nodes[current] = True
        current = current.nxt
    return None


# O(n)
# No extra space. Two pointers: p1 moves one node at a time, p2 two.
# If there's a loop of length L starting in k-th node, p2 will be in it by the time p1 reaches k.
# Once both are in the loop: distance between p2 and p1 < L.
# For every p1's step, p2 does two, so distance is 1 step less.
# So before p1 reaches k again, p2 will reach p1. That will happen after n < L steps.
# Encounter node:
# p1 ->  k + n
# p2 ->  2(k + n) = (k + n) + (k + n)    (p2 reached k, completed X loops and then encountered p1)
#                   -------   -------
#                     p1       X * L     --> (k + n) mod L = 0
# So, from k + n, after k steps pointer will reach k again.
# K is unknown, but (by definition), k is also k steps from the list's head.
# So, after first encounter, we move p2 to the head again, this time moving one node at a time.
# They'll meet again, this time in k
#
def first_node_in_loop_2(lst):
    # O(n)
    def aux_1st_encounter():
        p1 = lst.head
        p2 = lst.head.nxt
        while not p2.is_last() and not p2.nxt.is_last():
            if p1 is p2:
                return aux_2nd_encounter(p1.nxt)
            p1 = p1.nxt
            p2 = p2.nxt.nxt
        return None

    # O(n)
    def aux_2nd_encounter(p1):
        p2 = lst.head
        while not p1 is p2:
            p1 = p1.nxt
            p2 = p2.nxt
        return p1

    if lst.head.is_last():
        return None
    return aux_1st_encounter()


if __name__ == '__main__':
    l1 = MSinglyLinkedList().push(8)
    last = l1.head
    l1.push(7).push(6).push(5).push(4).push(3).push(2).push(1)
    last.nxt = l1.head.nxt.nxt
    print(first_node_in_loop_1(l1).data)  # 3
    print(first_node_in_loop_2(l1).data)  # 3

    l2 = MSinglyLinkedList().push(8).push(7).push(6).push(5).push(4).push(3).push(2).push(1)
    print(first_node_in_loop_1(l2))  # None
    print(first_node_in_loop_2(l2))  # None
