#!/usr/bin/python2
# https://www.hackerrank.com/challenges/tree-top-view/problem

class Node(object):
    def __init__(self, left_child = None, right_child = None, data = None):
        self.left = left_child
        self.right = right_child
        self.data = data

def top_view(root):
    def aux_left(current):
        if current.left:
            return aux_left(current.left) + [current.data]
        else:
            return [current.data]

    def aux_right(current):
        if current.right:
            return [current.data] + aux_right(current.right)
        else:
            return [current.data]

    if root:
        print ' '.join(map(str, (aux_left(root)[:-1] + aux_right(root))))


if __name__ == '__main__':
    top_view(Node(None, Node(None, Node(Node(None, Node(None, None, 4), 3), \
                                        Node(None, None, 6), \
                                        5), 2), 1))
    top_view(Node(Node(Node(None, None, 4), Node(None, Node(None, None, 6), 5), 2), \
                  Node(None, None, 3), \
                  1))
    top_view(None)
    top_view(Node(None, None, 4))
