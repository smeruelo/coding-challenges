class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self._buffer = [None] * capacity
        self._capacity = capacity
        self._write_index = 0
        self._read_index = None

    def read(self):
        if self._read_index is None:
            raise BufferEmptyException("There's no data to read.")
        data = self._buffer[self._read_index]
        if self._write_index is None:
            self._write_index = self._read_index
        nxt = (self._read_index + 1) % self._capacity
        self._read_index = nxt if nxt != self._write_index else None
        return data

    def write(self, data):
        if self._write_index is None:
            raise BufferFullException("There's no free slot to write in.")
        self._buffer[self._write_index] = data
        if self._read_index is None:
            self._read_index = self._write_index
        nxt = (self._write_index + 1) % self._capacity
        self._write_index = nxt if nxt != self._read_index else None

    def overwrite(self, data):
        if self._write_index is None:
            self._buffer[self._read_index] = data
            self._read_index = (self._read_index + 1) % self._capacity
        else:
            self.write(data)

    def clear(self):
        self._write_index = 0
        self._read_index = None
