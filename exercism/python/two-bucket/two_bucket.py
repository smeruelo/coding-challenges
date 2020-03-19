# https://exercism.io/my/solutions/b92199b7a5884fab83876d500a50200a


class Bucket():
    def __init__(self, size):
        self.size = size
        self.water = 0

    def has(self):
        return self.water

    def room(self):
        return self.size - self.water

    def pour(self, water=None):
        if water is None:
            water = self.has()
        self.water -= water

    def fill(self, water=None):
        if water is None:
            water = self.room()
        self.water += water


def measure(size_b1, size_b2, goal, start_bucket):
    buckets = {'one': Bucket(size_b1), 'two': Bucket(size_b2)}
    count = 0

    def other(bucket):
        return 'two' if bucket == 'one' else 'one'

    def op(code, bucket):
        nonlocal count
        if code == 'FILL':
            buckets[bucket].fill()
        if code == 'EMPTY':
            buckets[bucket].pour()
        if code == 'TRANSFER':
            litres = min(buckets[bucket].has(), buckets[other(bucket)].room())
            buckets[bucket].pour(litres)
            buckets[other(bucket)].fill(litres)
        count += 1

    if buckets[other(start_bucket)].room() == goal:
        return (2, other(start_bucket), buckets[start_bucket].room())

    while buckets[start_bucket].has() != goal and buckets[other(start_bucket)].has() != goal:
        if buckets[start_bucket].has() == 0:
            op('FILL', start_bucket)
        elif buckets[other(start_bucket)].room() == 0:
            op('EMPTY', other(start_bucket))
        else:
            op('TRANSFER', start_bucket)

    if buckets[start_bucket].has() == goal:
        return count, start_bucket, buckets[other(start_bucket)].has()
    return count, other(start_bucket), buckets[start_bucket].has()
