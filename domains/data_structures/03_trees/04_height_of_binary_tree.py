#!/usr/bin/python2
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

class Node(object):
    def __init__(self, left_child = None, right_child = None, data = None):
        self.left = left_child
        self.right = right_child
        self.data = data

def height(root):
    def aux(current, level):
        if current:
            return max(aux(current.left, level + 1), aux(current.right, level + 1))
        else:
            return level -1

    return aux(root, 0)


if __name__ == '__main__':
    t = Node(Node(Node(None, None, 1), None, 2), \
             Node(Node(None, None, 4), Node(None, Node(None, None, 7), 6), 5), \
             3)
    print height(t)
    print height(None)
    print height(Node(None, None, 1))
