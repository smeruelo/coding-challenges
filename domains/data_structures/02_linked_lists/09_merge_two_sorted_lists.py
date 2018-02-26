#!/usr/bin/python2
# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def create_list(lst):
    def aux(i):
        if i == len(lst):
            return None
        else:
            return Node(lst[i], aux(i + 1))
    return aux(0)

def print_list(head):
    output = ''
    current_node = head
    while current_node:
        output += ' ' + str(current_node.data)
        current_node = current_node.next
    if output:
        print output[1:]

def reverse(head):
    current = head
    previous = aux = None
    while current:
        aux = current.next
        current.next = previous
        previous = current
        current = aux
    return previous

def merge_lists(list_a, list_b):
    """ Merges two ordered lists into a new one"""

    def aux(node_a, node_b, node_c):
        if node_a and node_b:
            if node_a.data < node_b.data:
                return aux(node_a.next, node_b, Node(node_a.data, node_c))
            else:
                return aux(node_a, node_b.next, Node(node_b.data, node_c))
        elif node_a and not node_b:
            return aux(node_a.next, None, Node(node_a.data, node_c))
        elif not node_a and node_b:
            return aux(None, node_b.next, Node(node_b.data, node_c))
        else:  # not node_a and node_b
            return node_c

    return reverse(aux(list_a, list_b, None))

def read_list():
    if int(raw_input()) == 0:
        return []
    else:
        return map(int, raw_input().split())


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print_list(merge_lists(create_list(read_list()), create_list(read_list())))
