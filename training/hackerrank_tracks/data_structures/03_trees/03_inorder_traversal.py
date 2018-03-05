#!/usr/bin/python2
# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem

class Node(object):
    def __init__(self, left_child = None, right_child = None, data = None):
        self.left = left_child
        self.right = right_child
        self.data = data

def preorder(root):
    def aux(current):
        if current:
            return aux(current.left) + [current.data] + aux(current.right)
        else:
            return []

    if root:
        print ' '.join(map(str, aux(root)))


if __name__ == '__main__':
    t = Node(None, Node(None, Node(Node(None, Node(None, None, 4), 3), Node(None, None, 6), 5), 2), 1)
    preorder(t)
    preorder(None)
