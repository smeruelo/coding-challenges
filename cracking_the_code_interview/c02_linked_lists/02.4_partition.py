# Problem: Partition
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right
# partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from immutable_singly_linked_list import ISinglyLinkedList
from mutable_singly_linked_list import MSinglyLinkedList


# O(n)
def partition_im(lst, k):

    # O(n)
    def classify(smaller, bigger, rest):
        if rest.is_nil():
            return (smaller, bigger)
        if rest.head < k:
            return classify(smaller.push(rest.head), bigger, rest.tail)
        else:
            return classify(smaller, bigger.push(rest.head), rest.tail)

    # O(n)
    # There's no need to maintain the lists' order, so I won't use the library's concat
    # function to avoid lst1 being reversed.
    def concat_no_reverse(lst1, lst2):
        def aux(new, rest1):
            if rest1.is_nil():
                return new
            return aux(new.push(rest1.head), rest1.tail)
        return aux(lst2, lst1)

    return concat_no_reverse(*classify(ISinglyLinkedList(), ISinglyLinkedList(), lst))


# O(n)
def partition_m(lst, k):
    smaller = MSinglyLinkedList()
    bigger = MSinglyLinkedList()

    current_node = lst.head
    while not current_node is None:
        if current_node.data < k:
            smaller.push(current_node.data)
        else:
            bigger.push(current_node.data)
        current_node = current_node.nxt

    lst.head = smaller.concat(bigger).head
    return lst


if __name__ == '__main__':
    l1 = ISinglyLinkedList().push(0).push(7).push(3).push(2).push(7).push(1).push(0)
    l2 = partition_im(l1, 3)
    print(f'{l1}\n{l2}')

    l3 = MSinglyLinkedList().push(0).push(7).push(3).push(2).push(7).push(1).push(0)
    partition_m(l3, 3)
    print(l3)
