#!/usr/bin/python2
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# O(n)
def checkBST(root):
    def aux(node):
        min_subtree = max_subtree = node.data
        bst_subtree = True
        if node.left:
            bst_left, min_left, max_left = aux(node.left)
            bst_subtree = bst_left and max_left < node.data
            min_subtree = min(min_left, min_subtree)
            max_subtree = max(max_left, max_subtree)
        if node.right:
            bst_right, min_right, max_right = aux(node.right)
            bst_subtree = bst_right and bst_subtree and min_right > node.data
            min_subtree = min(min_right, min_subtree)
            max_subtree = max(max_right, max_subtree)
        print node.data, min_subtree, max_subtree, bst_subtree
        return (bst_subtree, min_subtree, max_subtree)

    if root:
        return aux(root)[0]
    else:
        return True


if __name__ == '__main__':
    yes = Node(3, Node(2, Node(1), None), Node(6, Node(4, None, Node(5)), Node(7)))
    no1 = Node(3, Node(2, Node(1), None), Node(6, Node(4, None, Node(3)), Node(7)))
    no2 = Node(5, Node(2, Node(1), Node(3)), Node(6, Node(4), Node(7)))
    print checkBST(yes), 'True'
    print checkBST(no1), 'False'
    print checkBST(no2), 'False'
    print checkBST(None), 'True'
