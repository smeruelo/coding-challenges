#!/usr/bin/python2
# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

#   a --- a --- a --- a                        a = length of the section unique to a
#                      \                       b = length of the section unique to b
#                       c --- c--- c           c = length of the common section
#                      /
#         b --- b --- b                        a + c + b  =  b + c + a

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def find_merge_node(head_a, head_b):
    current_a = head_a
    current_b = head_b
    while current_a != current_b:
        if current_a == None:
            current_a = head_b
        else:
            current_a = current_a.next
        if current_b == None:
            current_b = head_a
        else:
            current_b = current_b.next
    return current_a.value
