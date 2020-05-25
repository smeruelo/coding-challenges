from copy import deepcopy


class Zipper:

    def __init__(self, value, left, right, zipper=[]):
        self._value = value
        self._left = left
        self._right = right
        self._zipper = zipper

    @staticmethod
    def from_tree(tree):
        if tree == None:
            return None
        return Zipper(tree["value"], Zipper.from_tree(tree["left"]), Zipper.from_tree(tree["right"]), [])

    def value(self):
        return self._value

    def set_value(self, value):
        return Zipper(value, self._left, self._right, deepcopy(self._zipper))

    def left(self):
        if self._left == None:
            return None
        return Zipper(self._left._value, self._left._left, self._left._right, self._zipper + [("left", self)])

    def set_left(self, branch):
        return Zipper(self.value(), Zipper.from_tree(branch), self._right, deepcopy(self._zipper))

    def right(self):
        if self._right == None:
            return None
        return Zipper(self._right._value, self._right._left, self._right._right, self._zipper + [("right", self)])

    def set_right(self, branch):
        return Zipper(self.value(), self._left, Zipper.from_tree(branch), deepcopy(self._zipper))

    def up(self):
        if self._zipper == []:
            return None
        _, parent = self._zipper[-1]
        return Zipper(parent.value(), parent._left, parent._right, self._zipper[:-1])

    def down_tree(self):
        left_branch = None if self._left == None else self._left.down_tree()
        right_branch = None if self._right == None else self._right.down_tree()
        return {"value": self.value(), "left": left_branch, "right": right_branch}

    def to_tree(self):
        down = self.down_tree()
        if self._zipper == []:
            return down
        
        move, parent = self._zipper[-1]
        if move == "left":
            right_branch = None if parent._right == None else parent._right.down_tree()
            tree = {"value": parent.value(), "left": down, "right": right_branch}
        elif move == "right":
            left_branch = None if parent._left == None else parent._left.down_tree()
            tree = {"value": parent.value(), "left": left_branch, "right": down}

        for move, parent in reversed(self._zipper[:-1]):
            if move == "left":
                right_branch = None if parent._right == None else parent._right.down_tree()
                tree = {"value": parent.value(), "left": tree, "right": right_branch}
            elif move == "right":
                left_branch = None if parent._left == None else parent._left.down_tree()
                tree = {"value": parent.value(), "left": left_branch, "right": tree}
        return tree
