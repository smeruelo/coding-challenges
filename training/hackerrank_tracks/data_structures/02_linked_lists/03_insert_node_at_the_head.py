#!/usr/bin/python2
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

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

def insert_head(head, data):
    return Node(data, head)


if __name__ == '__main__':
    print_list(insert_head(create_list([2, 3, 4]), 1)); print
    print_list(insert_head(create_list([]), 1))
