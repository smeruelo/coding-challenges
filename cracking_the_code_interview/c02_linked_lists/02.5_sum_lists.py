# Problem: Sum Lists
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from immutable_singly_linked_list import ISinglyLinkedList


# O(n), where n = max{n1, n2}
def sum_reverse_order(lst1, lst2):
    def aux(rest1, rest2, carry, out):
        if rest1.is_nil() and rest2.is_nil():
            return out.push(carry).reverse() if carry > 0 else out.reverse()
        if not rest1.is_nil() and not rest2.is_nil():
            s = carry + rest1.head + rest2.head
            return aux(rest1.tail, rest2.tail, s // 10, out.push(s % 10))
        if not rest1.is_nil() and rest2.is_nil():
            s = carry + rest1.head
            return aux(rest1.tail, rest2, s // 10, out.push(s % 10))
        if rest1.is_nil() and not rest2.is_nil():
            s = carry + rest2.head
            return aux(rest1, rest2.tail, s // 10, out.push(s % 10))

    return aux(lst1, lst2, 0, ISinglyLinkedList())


# O(n)
# it takes extra O(n) space (n simultaneous recursive calls)
def sum_forward_order(lst1, lst2):

    # O(k), where k = max{n1, n2} - min{n1, n2}
    def pad_with_zeros(lst, k):
        if k == 0:
            return lst
        return pad_with_zeros(lst.push(0), k - 1)

    # O(n1) + O(n2) + O(max{n1, n2} - min{n1, n2}) --> O(max{n1, n2})
    n1 = lst1.length()
    n2 = lst2.length()
    if n1 > n2:
        lst2 = pad_with_zeros(lst2, n1 - n2)
    if n2 > n1:
        lst1 = pad_with_zeros(lst1, n2 - n1)

    out = ISinglyLinkedList()

    # O(n), where n = max{n1, n2}
    def aux(current1, current2):
        nonlocal out
        if current1.is_nil() and current2.is_nil():
            return 0
        s = current1.head + current2.head + aux(current1.tail, current2.tail)
        out = out.push(s % 10)
        return s // 10

    carry = aux(lst1, lst2)
    return out.push(carry) if carry > 0 else out


if __name__ == '__main__':
    l1 = ISinglyLinkedList().push(6).push(1).push(7)
    l2 = ISinglyLinkedList().push(9).push(5).push(0).push(4)
    print(f'{l1}\n{l2}\n{sum_reverse_order(l1, l2)}')

    l3 = ISinglyLinkedList().push(7).push(1).push(6)
    l4 = ISinglyLinkedList().push(5).push(9).push(8).push(9)
    print(f'{l3}\n{l4}\n{sum_forward_order(l3, l4)}')
