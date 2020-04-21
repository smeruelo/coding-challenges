# https://exercism.io/my/solutions/9fbd9656b7c243a2b4f9088fed1398bc

NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.attrs = dict()
        self.nodes = []
        self.edges = []

        if data is None:
            return

        try:
            iter_data = iter(data)
        except Exception:
            raise TypeError('Malformed graph.')

        for tuple_data in iter_data:
            if len(tuple_data) < 2:
                raise TypeError('Malformed graph.')
            code, *args = tuple_data
            if code == ATTR:
                if len(args) != 2:
                    raise ValueError('Malformed attribute.')
                attr, value = args
                self.attrs[attr] = value
            elif code == NODE:
                if len(args) != 2:
                    raise ValueError('Malformed node.')
                self.nodes.append(Node(*args))
            elif code == EDGE:
                if len(args) != 3:
                    raise ValueError('Malformed edge.')
                self.edges.append(Edge(*args))
            else:
                raise ValueError('Malformed graph.')
