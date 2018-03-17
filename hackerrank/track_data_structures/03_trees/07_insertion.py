#!/usr/bin/python2
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

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
        print ' '.join(map(lambda x: str(x.data) if x else '-', nodes))

def insert(root, value):
    if root:
        if value < root.data:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root
    else:
        return Node(None, None, value)


if __name__ == '__main__':
    t = Node(Node(Node(None, None, 1), Node(None, None, 3), 2), Node(None, None, 7), 4)
    t = insert(t, 6)
    level_order(t)
    print '4 2 7 1 3 6 - - - - - - -'

    t = Node(Node(Node(None, None, 1), Node(None, None, 3), 2), Node(None, None, 7), 5)
    t = insert(t, 4)
    level_order(t)
    print '5 2 7 1 3 - - - - - 4 - -'

    t = None
    t = insert(t, 3)
    level_order(t)
    print '3 - -'

    t = Node(None, None, 4)
    t = insert(t, 3)
    level_order(t)
    print '4 3 - - -'

    t = Node(None, None, 4)
    t = insert(t, 5)
    level_order(t)
    print '4 - 5 - -'
