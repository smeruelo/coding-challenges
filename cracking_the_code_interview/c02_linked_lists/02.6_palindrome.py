#! /usr/bin/python3
from immutable_singly_linked_list import ISinglyLinkedList


# O(n), where n = min{n1, n2}
def equal(lst1, lst2):
    if lst1.is_nil() or lst2.is_nil():
        return lst1.is_nil() and lst2.is_nil()
    if lst1.head == lst2.head:
        return equal(lst1.tail, lst2.tail)
    else:
        return False


# O(n) + O(n) --> O(n)
def palindrome_1(lst):
    # Reverse and compare

    rev = lst.reverse()
    return equal(lst, rev)


# O(n/2) + O(n/2) = O(n/2) --> O(n)
def palindrome_2(lst):
    # Reverse half the list only
    # Since we don't know the size --> two pointers, one makes 1-node steps, the other 2-node steps

    # O(n/2)
    def half_reverse(rev, p1, p2):
        if p2.is_nil():
            return (p1, rev)
        if p2.tail.is_nil():
            return (p1.tail, rev)
        return half_reverse(rev.push(p1.head), p1.tail, p2.tail.tail)

    # O(n/2)
    return equal(*half_reverse(ISinglyLinkedList(), lst, lst))


# O(n)
# it takes extra O(n) space (n simultaneous recursive calls)
def palindrome_3(lst):
    # Recursive

    # O(n)
    n = lst.length()

    # O(n)
    def aux(i, current):
        # Decrementing the length by 2 on every call, to detect the middle of the list
        # Returns a pointer to the current node's opposite.

        if i == 1:
            return (True, current.tail)
        if i == 0:
            return (True, current)
        palindrome_so_far, opposite = aux(i - 2, current.tail)
        if palindrome_so_far:
            if current.head == opposite.head:
                return (True, opposite.tail)
        return (False, opposite.tail)

    result, _ = aux(n, lst)
    return result


if __name__ == '__main__':
    l1 = ISinglyLinkedList().push(2).push(1).push(7).push(1).push(2)
    l2 = ISinglyLinkedList().push(2).push(1).push(7).push(7).push(1).push(2)
    l3 = ISinglyLinkedList().push(2).push(1).push(5).push(7).push(1).push(2)
    l4 = ISinglyLinkedList()
    print(palindrome_1(l1), palindrome_1(l2), palindrome_1(l3), palindrome_1(l4))
    print(palindrome_2(l1), palindrome_2(l2), palindrome_2(l3), palindrome_2(l4))
    print(palindrome_3(l1), palindrome_3(l2), palindrome_3(l3), palindrome_3(l4))
