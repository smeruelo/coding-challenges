#!/usr/bin/python2
# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

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

def remove_duplicates(head):
    if head:
        previous = head
        current = head.next
        while current:
            if current.data == previous.data:
                previous.next = current.next
            else:
                previous = current
            current = current.next
    return head

def read_list():
    if int(raw_input()) == 0:
        return []
    else:
        return map(int, raw_input().split())


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print_list(remove_duplicates(create_list(read_list())))
