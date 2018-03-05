#!/usr/bin/python2
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

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


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        if int(raw_input()) == 0:
            lst = []
        else:
            lst = raw_input().split()
        print_list(create_list(lst))
