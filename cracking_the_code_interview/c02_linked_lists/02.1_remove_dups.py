# Problem: Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from collections import defaultdict
from immutable_singly_linked_list import ISinglyLinkedList


# O(n)
# Extra space
def remove_dups_1(lst):
    appeared = defaultdict(bool)
    def aux(no_dups, rest):
        if rest.is_nil():
            return no_dups
        if appeared[rest.head]:
            return aux(no_dups, rest.tail)
        appeared[rest.head] = True
        return aux(no_dups.push(rest.head), rest.tail)

    return aux(ISinglyLinkedList(), lst).reverse()


# O(n * n)
# No extra space
def remove_dups_2(lst):

    # O(n)
    def is_member(element, rest):
        if rest.is_nil():
            return False
        if element == rest.head:
            return True
        return is_member(element, rest.tail)

    # O(n * n)
    def aux(no_dups, rest):
        if rest.is_nil():
            return no_dups
        if is_member(rest.head, no_dups):
            return aux(no_dups, rest.tail)
        else:
            return aux(no_dups.push(rest.head), rest.tail)

    return aux(ISinglyLinkedList(), lst).reverse()


if __name__ == '__main__':
    lst_dups = ISinglyLinkedList().push(0).push(7).push(3).push(2).push(7).push(1).push(0)
    print(lst_dups)
    print(remove_dups_1(lst_dups))
    print(remove_dups_2(lst_dups))
