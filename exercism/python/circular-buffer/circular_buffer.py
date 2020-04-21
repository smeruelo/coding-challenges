class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self._buffer = []
        self._capacity = capacity

    def read(self):
        if self._empty():
            raise BufferEmptyException("There's no data to read.")
        return self._buffer.pop(0)

    def write(self, data):
        if self._full():
            raise BufferFullException("There's no free slot to write in.")
        self._buffer.append(data)

    def overwrite(self, data):
        if self._full():
            _ = self._buffer.pop(0)
        self._buffer.append(data)

    def clear(self):
        self._buffer = []

    def _empty(self):
        return len(self._buffer) == 0

    def _full(self):
        return len(self._buffer) >= self._capacity
