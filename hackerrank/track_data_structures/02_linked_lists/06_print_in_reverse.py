#!/usr/bin/python2
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

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

def print_reverse(head):
    def aux(node):
        if node:
            return aux(node.next) + '\n' + str(node.data)
        else:
            return ''

    output = aux(head)
    if output:
        print output[1:]


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        print_reverse(create_list(raw_input().split()))
