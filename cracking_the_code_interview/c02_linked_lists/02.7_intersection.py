from mutable_singly_linked_list import MSinglyLinkedList


# O(n)
def len_and_last(lst):
    """Returns (n, node), where n = length of the list, and node = its last node"""
    def aux(i, current):
        if not current.nxt:
            return (i, current)
        return aux(i + 1, current.nxt)

    if lst.is_empty():
        return (0, lst)
    return aux(1, lst.head)


# O(n1 + n2)
# If two lists intersect, their last node will be the same.
# I first check that, and calculate lists lengths at the same time.
# Then I advance enough nodes in the longest list so I can then
# compare two lists of equal length.
def intersecting_node(lst1, lst2):

    # O(k)
    def kth_node_pointer(current, k):
        if k == 0:
            return current
        return kth_node_pointer(current.nxt, k - 1)

    # O(n)
    def aux(current1, current2):
        if current1 is current2:
            return current1
        return aux(current1.nxt, current2.nxt)

    n1, last1 = len_and_last(lst1)  # O(n1)
    n2, last2 = len_and_last(lst2)  # O(n2)
    if last1 is last2:
        if n2 > n1:
            return aux(l1.head, kth_node_pointer(l2.head, n2 - n1))
        if n1 > n2:
            return aux(kth_node_pointer(l1.head, n1 - n2), l2.head)
        return aux(l1.head, l2.head)
    return None


if __name__ == '__main__':
    l1 = MSinglyLinkedList().push(3).push(2).push(1)
    l2 = MSinglyLinkedList().push(5).push(4)
    l3 = MSinglyLinkedList().push(5).push(4)
    l1.concat(l2)
    l2.push(33).push(22)
    #
    #  l1:  ->  1 ->  2 ->  3
    #                         \
    #                           -> 4 -> 5
    #                         /
    #  l2:           22 -> 33
    #
    #  l3:                      -> 4 -> 5
    #
    print(intersecting_node(l1, l2).data)  # 4
    print(intersecting_node(l1, l3))       # None
