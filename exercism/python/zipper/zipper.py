from copy import deepcopy


class Zipper:

    def __init__(self, tree, zipper=[]):
        self._focus = tree
        self._zipper = zipper

    @staticmethod
    def from_tree(tree):
        return Zipper(deepcopy(tree))

    def value(self):
        if self._focus == None:
            raise Exception("nope")
        return self._focus['value']

    def set_value(self, value):
        if self._focus == None:
            raise Exception("nope")
            # tree = {"value": value, "left": None, "right": None}
            # last, parent = self._zipper[-1]
            # if last == 'left':
        else:
            tree = deepcopy(self._focus)
            tree['value'] = value
        return Zipper(tree, self._zipper)

    def left(self):
        if self._focus == None:
            raise Exception("nope")
        if self._focus['left'] == None:
            return None
        return Zipper(self._focus["left"], self._zipper + [("left", self._focus)])

    def set_left(self, branch):
        if self._focus == None:
            raise Exception("nope")
        tree = deepcopy(self._focus)
        tree['left'] = branch
        return Zipper(tree, self._zipper)

    def right(self):
        if self._focus == None:
            raise Exception("nope")
        if self._focus['right'] == None:
            return None
        return Zipper(self._focus["right"], self._zipper + [("right", self._focus)])

    def set_right(self, branch):
        if self._focus == None:
            raise Exception("nope")
        tree = deepcopy(self._focus)
        tree['right'] = branch
        return Zipper(tree, self._zipper)

    def up(self):
        if self._zipper == []:
            return None
        _, parent = self._zipper[-1]
        return Zipper(parent, self._zipper[:-1])

    def to_tree(self):
        def rec(tree, zipper):
            if zipper == []:
                tree[move]
                return tree
            move, parent = self._zipper[0]

        tree = dict()
        move, parent = self._zipper[0]
        rec(parent, move, self._zipper[1:])
        return tree
