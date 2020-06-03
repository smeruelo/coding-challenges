from string import ascii_uppercase


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse_prop_name(s, i):
    name = ""
    while i < len(s) and s[i] != "[":
        if s[i] in "();]" or s[i] not in ascii_uppercase:
            raise ValueError("Syntax Error.")
        name += s[i]
        i += 1
    if i == len(s):
        raise ValueError("Syntax Error.")
    return name, i


def parse_prop_value(s, i):
    if s[i] != "[":
        raise ValueError("Syntax Error.")
    i += 1
    value = ""
    while i < len(s) and s[i] != "]":
        if s[i] == "\\" and i + 1 < len(s):
            i += 1
        elif s[i] in "();[":
            raise ValueError("Syntax Error.")
        value += s[i]
        i += 1
    if i == len(s):
        raise ValueError("Syntax Error.")
    return value.replace("\t", " "), i+1


def parse_node(s, i):
    if s[i] != ";":
        raise ValueError("Syntax Error.")
    i += 1
    properties = dict()
    while i < len(s) and s[i] not in ";()":
        name, i = parse_prop_name(s, i)
        values = []
        while s[i] == "[":
            value, i = parse_prop_value(s, i)
            values.append(value)
        properties[name] = values
    if i == len(s):
        raise ValueError("Syntax Error.")
    if s[i] == ";":
        child, i = parse_node(s, i)
        return SgfTree(properties, [child]), i
    if s[i] == "(":
        left_child, i = parse_tree(s, i)
        right_child, i = parse_tree(s, i)
        return SgfTree(properties, [left_child, right_child]), i
    if s[i] == ")":
        return SgfTree(properties), i


def parse_tree(s ,i):
    if s[i] != "(":
        raise ValueError("Syntax Error")
    tree, i = parse_node(s, i+1)
    if s[i] != ")":
        raise ValueError("Syntax Error")
    return tree, i+1


def parse(s):
    if len(s) == 0:
        raise ValueError("Syntax Error")
    tree, i = parse_tree(s, 0)
    if i != len(s):
        raise ValueError("Syntax Error")
    return tree
