#!/usr/bin/python2
# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

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

def get_node(head, position):
    def aux(node):
        if node.next:
            next_data, next_pos = aux(node.next)
            current_pos = next_pos + 1
            if position == current_pos:
                return (node.data, current_pos)
            else:
                return (next_data, current_pos)
        else:
            if position == 0:
                return (node.data, 0)
            else:
                return (None, 0)

    return aux(head)[0]

def read_list():
    if int(raw_input()) == 0:
        return []
    else:
        return map(int, raw_input().split())


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        lst = read_list()
        pos = int(raw_input())
        print get_node(create_list(lst), pos)
