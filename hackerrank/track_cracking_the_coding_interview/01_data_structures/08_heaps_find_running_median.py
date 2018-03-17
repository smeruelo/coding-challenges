#!/usr/bin/python2
# https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

from Queue import PriorityQueue

class Heap:
    # Wrap around PriorityQueue so don't have to worry if it's a max heap or min heap

    def __init__(self, max_heap=False):
        self.sign = -1 if max_heap else 1
        self.heap = PriorityQueue()

    def put(self, n):
        self.heap.put(self.sign * n)

    def get(self):
        return self.sign * self.heap.get()

    def peek(self):
        n = self.heap.get()
        self.heap.put(n)
        return self.sign * n

    def qsize(self):
        return self.heap.qsize()

    def empty(self):
        return self.heap.empty()


def medians(nums):
    # Two heaps, one for the elements to the left of the median, one for the ones to the right
    # Left heap is a max_heap, right one is a min_one
    # Both heaps should have always the same size
    left = Heap(max_heap=True)
    right = Heap()

    # Treat the first two numbers appart
    results = [nums[0]]
    if len(nums) < 2:
        left.put(nums[0])
    else:
        left.put(min(nums[0], nums[1]))
        right.put(max(nums[0], nums[1]))
        results.append((nums[0] + nums[1])/2)

    for i in nums[2:]:
        # Store the num in one of the heaps
        if i > left.peek() and i < right.peek():
            if left.qsize() <= right.qsize():
                left.put(i)
            else:
                right.put(i)
        elif i <= left.peek():
            left.put(i)
            if left.qsize() - right.qsize() > 1:
                right.put(left.get())
        else:
            right.put(i)
            if right.qsize() - left.qsize() > 1:
                left.put(right.get())

        # Calculate the new median
        if (left.qsize() + right.qsize()) % 2 == 0:
            median = (left.peek() + right.peek()) / 2
        elif left.qsize() > right.qsize():
            median = left.peek()
        else:
            median = right.peek()
        results.append(median)

    return results


if __name__ == '__main__':
    n = int(raw_input())
    for i in medians([float(raw_input()) for _ in xrange(n)]):
        print "{0:.1f}".format(i)
