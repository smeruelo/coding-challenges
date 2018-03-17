#!/usr/bin/python2
# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

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

def delete_nth(head, position):
    if position == 0:
        return head.next
    else:
        current_node = head
        for i in range(1, position):
            current_node = current_node.next
        current_node.next = current_node.next.next
        return head


if __name__ == '__main__':
    print_list(delete_nth(create_list([0, 1, 2, 8, 3]), 3)); print
    print_list(delete_nth(create_list([0, 1, 2, 3]), 3)); print
    print_list(delete_nth(create_list([8, 0, 1, 2]), 0)); print
    print_list(delete_nth(create_list([0]), 0))
