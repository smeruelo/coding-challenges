# https://exercism.io/my/solutions/47d3b73443d742cb9eadd05880c5018b


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __le__(self, other):
        return int(self.data) <= int(other.data)

    def __str__(self):
        return f'TreeNode("{self.data}", {self.left}, {self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            self.insert(TreeNode(item), self.root)

    def insert(self, node, parent):
        if node <= parent:
            if parent.left:
                self.insert(node, parent.left)
            else:
                parent.left = node
        else:
            if parent.right:
                self.insert(node, parent.right)
            else:
                parent.right = node

    def data(self):
        return self.root

    def sorted_data(self):
        def in_order(node):
            if node is None:
                return []
            return in_order(node.left) + [node.data] + in_order(node.right)

        return in_order(self.root)

    def __str__(self):
        return str(self.root)
