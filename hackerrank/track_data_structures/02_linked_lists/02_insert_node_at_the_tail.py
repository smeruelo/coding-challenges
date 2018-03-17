#!/usr/bin/python2
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    current_node = head
    while current_node:
        print str(current_node.data)
        current_node = current_node.next

def create_list(lst):
    def aux(i):
        if i == len(lst):
            return None
        else:
            return Node(lst[i], aux(i + 1))
    return aux(0)

def Insert(head, data):
    new_node = Node(data, None)
    if head:
        current_node = head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return head
    else:
        return new_node


if __name__ == '__main__':
    print_list(Insert(create_list([1, 2, 3, 4]), 5)); print
    print_list(Insert(create_list([]), 1))
