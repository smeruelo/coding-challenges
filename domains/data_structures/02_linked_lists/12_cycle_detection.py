#!/usr/bin/python2
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    # Two pointers, p1 advances one node at a time, p2 two nodes
    # If there's a cycle, they'll eventually meet
    p1 = p2 = head
    while p1 and p2:
        p1 = p1.next
        p2 = p2.next.next if p2.next else None
        if p1 and p1 == p2 :
            return True
    return False
