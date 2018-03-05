#!/usr/bin/python2
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def print_list(head):
    output = ''
    current_node = head
    while current_node:
        output += ' ' + str(current_node.data)
        current_node = current_node.next
    if output:
        print output[1:]

def create_list(lst):
    def aux(prev, i):
        if i == len(lst):
            return None
        else:
            current = Node(lst[i], None, prev)
            current.next = aux(current, i + 1)
            return current
    return aux(None, 0)

def reverse(head):
    if head:
        current = head
        while current.next:
            aux = current.next
            current.next = current.prev
            current.prev = aux
            current = aux
        current.next = current.prev
        current.prev = None
        return current
    else:
        return head


if __name__ == '__main__':
    print_list(reverse(create_list([3, 2, 1])))
    print_list(reverse(create_list([1])))
    print_list(reverse(create_list([])))
