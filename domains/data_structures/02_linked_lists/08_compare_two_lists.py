#!/usr/bin/python2
# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

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

def compare(head_a, head_b):
    current_a = head_a
    current_b = head_b
    while current_a and current_b:
        if current_a.data != current_b.data:
            return int(False)
        current_a = current_a.next
        current_b = current_b.next
    return int(not current_a and not current_b)


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        list_a = create_list(raw_input().split())
        _ = raw_input()
        list_b = create_list(raw_input().split())
        print compare(list_a, list_b)
