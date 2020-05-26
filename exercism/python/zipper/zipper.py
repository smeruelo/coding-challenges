# https://exercism.io/my/solutions/1a1c96a4fa304f4aa9f72b99a9cf8411

from copy import deepcopy


LEFT = "left"
RIGHT = "right"
VALUE = "value"
OPPOSITE = {LEFT: RIGHT, RIGHT: LEFT}


class Zipper:

    def __init__(self, value, left, right, zipper=[]):
        self._value = value
        self._left = left
        self._right = right
        self._zipper = zipper

    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        return Zipper(
            tree[VALUE],
            Zipper.from_tree(tree[LEFT]),
            Zipper.from_tree(tree[RIGHT]),
            []
        )

    def value(self):
        return self._value

    def set_value(self, value):
        return Zipper(value, self._left, self._right, deepcopy(self._zipper))

    def left(self):
        if self._left is None:
            return None
        return Zipper(
            self._left._value,
            self._left._left,
            self._left._right,
            self._zipper + [(LEFT, self)]
        )

    def set_left(self, branch):
        return Zipper(self.value(), Zipper.from_tree(branch), self._right, deepcopy(self._zipper))

    def right(self):
        if self._right is None:
            return None
        return Zipper(
            self._right._value,
            self._right._left,
            self._right._right,
            self._zipper + [(RIGHT, self)]
        )

    def set_right(self, branch):
        return Zipper(self.value(), self._left, Zipper.from_tree(branch), deepcopy(self._zipper))

    def up(self):
        if self._zipper == []:
            return None
        _, parent = self._zipper[-1]
        return Zipper(parent.value(), parent._left, parent._right, self._zipper[:-1])

    def branch(self, choice):
        return self._left if choice == LEFT else self._right

    def current_to_bottom_tree(self):
        left_branch = None if self._left is None else self._left.current_to_bottom_tree()
        right_branch = None if self._right is None else self._right.current_to_bottom_tree()
        return {"value": self.value(), LEFT: left_branch, RIGHT: right_branch}

    def to_tree(self):
        down = self.current_to_bottom_tree()
        if self._zipper == []:
            return down

        choice, parent = self._zipper[-1]
        if parent.branch(OPPOSITE[choice]) is None:
            other_branch = None
        else:
            other_branch = parent.branch(OPPOSITE[choice]).current_to_bottom_tree()
        tree = {"value": parent.value(), choice: down, OPPOSITE[choice]: other_branch}

        for choice, parent in reversed(self._zipper[:-1]):
            if parent.branch(OPPOSITE[choice]) is None:
                other_branch = None
            else:
                other_branch = parent.branch(OPPOSITE[choice]).current_to_bottom_tree()
            tree = {"value": parent.value(), choice: tree, OPPOSITE[choice]: other_branch}
        return tree
