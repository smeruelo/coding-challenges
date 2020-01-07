# Very bad solution
# We occupy the cells secuencially. In each cell we store the item and the index of the next one.
# The first 3 cells store the heads of the 3 stacks.
# pop() leaves empty cells that are never reused.

class ThreeStacks():
    def __init__(self):
        self._array = [None, None, None]
        self._first_free_cell = 3

    def validated_stack_number(f):
        def f_wrapper(*args, **kwargs):
            stack = args[1]
            if stack < 0 or stack > 2:
                raise WrongStackNumberError('"stack" must be an integer in [0-2]')
            return f(*args, **kwargs)
        return f_wrapper

    @validated_stack_number
    def pop(self, stack):
        if self._array[stack] is None:
            raise EmptyStackError(f'Stack {stack}')
        head = self._array[stack]
        item, new_head = self._array[head]
        self._array[head] = 'UNUSED'
        self._array[stack] = new_head
        return item

    @validated_stack_number
    def push(self, stack, item):
        head = self._array[stack]
        self._array.append((item, head))
        self._array[stack] = self._first_free_cell
        self._first_free_cell += 1
        return self

    @validated_stack_number
    def peek(self, stack):
        if self._array[stack] is None:
            raise EmptyStackError(f'Stack {stack}')
        head = self._array[stack]
        item, _ = self._array[head]
        return item

    @validated_stack_number
    def is_empty(self, stack):
        return self._array[stack] is None

    def __repr__(self):
        def traverse(stack):
            current = self._array[stack]
            while current is not None:
                item, current = self._array[current]
                yield item

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


class WrongStackNumberError(Exception):
    pass
