class ThreeStacks():
    SIZE = 3

    def __init__(self):
        self._array = [None] * 3 * self.SIZE
        self._size = [0, 0, 0]

    def validated_stack_number(f):
        def f_wrapper(*args, **kwargs):
            stack = args[1]
            if stack < 0 or stack > 2:
                raise WrongStackNumberError('"stack" must be an integer in [0-2]')
            return f(*args, **kwargs)
        return f_wrapper

    @validated_stack_number
    def size(self, stack):
        return self._size[stack]

    def _index(self, stack, i):
        return (stack * self.SIZE) + i

    @validated_stack_number
    def pop(self, stack):
        if self.size(stack) == 0:
            raise EmptyStackError(f'Stack {stack}')
        i = self._index(stack, self.size(stack) - 1)
        self._size[stack] -= 1
        return self._array[i]

    @validated_stack_number
    def push(self, stack, item):
        if self.size(stack) == self.SIZE:
            raise FullStackError(f'Stack {stack}')
        i = self._index(stack, self.size(stack))
        self._array[i] = item
        self._size[stack] += 1
        return self

    @validated_stack_number
    def peek(self, stack):
        if self.size(stack) == 0:
            raise EmptyStackError(f'Stack {stack}')
        i = self._index(stack, self.size(stack) - 1)
        return self._array[i]

    @validated_stack_number
    def is_empty(self, stack):
        return self.size(stack) == 0

    def __repr__(self):
        def traverse(stack):
            current = self.size(stack) - 1
            while current >= 0:
                yield self._array[self._index(stack, current)]
                current -= 1

        def repr(stack):
            gen = traverse(stack)
            out = ''
            try:
                while True:
                    out += f' -> {str(next(gen))}'
            except StopIteration:
                return f'{out}.'

        return f'{repr(0)}\n{repr(1)}\n{repr(2)}'


class EmptyStackError(Exception):
    pass


class FullStackError(Exception):
    pass


class WrongStackNumberError(Exception):
    pass
