#!/usr/bin/python2
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

class Node(object):
    def __init__(self, left_child = None, right_child = None, data = None):
        self.left = left_child
        self.right = right_child
        self.data = data

def level_order(root):
    nodes = [root]
    i = 0
    while i < len(nodes):
        current = nodes[i]
        if current:
            nodes.extend([current.left, current.right])
        i += 1
    if root:
        print ' '.join(map(lambda x: str(x.data), filter(lambda x: x, nodes)))


if __name__ == '__main__':
    level_order(Node(None, Node(None, Node(Node(None, Node(None, None, 4), 3), \
                                        Node(None, None, 6), \
                                        5), 2), 1))
    level_order(Node(Node(Node(None, None, 4), Node(None, Node(None, None, 6), 5), 2), \
                  Node(None, None, 3), \
                  1))
    level_order(None)
    level_order(Node(None, None, 4))
