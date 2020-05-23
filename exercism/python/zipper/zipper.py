from copy import deepcopy


class Zipper:

    def __init__(self, tree, zipper=[]):
        self._focus = tree
        self._zipper = zipper

    @staticmethod
    def from_tree(tree):
        return Zipper(deepcopy(tree))

    def value(self):
        return self._focus['value']

    def set_value(self, value):
        tree = deepcopy(self._focus)
        tree['value'] = value
        return Zipper(tree, deepcopy(self._zipper))

    def left(self):
        if self._focus['left'] == None:
            return None
        return Zipper(self._focus["left"], self._zipper + [("left", self._focus)])

    def set_left(self, branch):
        tree = deepcopy(self._focus)
        tree['left'] = branch
        return Zipper(tree, deepcopy(self._zipper))

    def right(self):
        if self._focus['right'] == None:
            return None
        return Zipper(self._focus["right"], self._zipper + [("right", self._focus)])

    def set_right(self, branch):
        tree = deepcopy(self._focus)
        tree['right'] = branch
        return Zipper(tree, deepcopy(self._zipper))

    def up(self):
        if self._zipper == []:
            return None
        _, parent = self._zipper[-1]
        return Zipper(parent, self._zipper[:-1])

    def to_tree(self):
        def rec(tree, move, zipper):
            if zipper == []:
                tree[move] = self._focus
                return
            nxt_move, parent = zipper[0]
            rec(parent, nxt_move, zipper[1:])

        if self._zipper == []:
            return self._focus
        move, parent = self._zipper[0]
        tree = dict(parent)
        rec(tree, move, self._zipper[1:])
        return tree
