#!/usr/bin/python2
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

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

def sorted_insert(head, data):
    if head:
        current = head
        while current.next and current.data < data:
            current = current.next
        if current.data >= data:
            new = Node(data, current, current.prev)
            if current.prev:
                current.prev.next = new
                current.prev = new
                return head
            else:
                current.prev = new
                return new
        else:
            new = Node(data, None, current)
            current.next = new
            return head
    else:
        return Node(data, None, None)


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        lst = None
        for i in map(int, raw_input().split()):
            lst = sorted_insert(lst, i)
        print_list(lst)
