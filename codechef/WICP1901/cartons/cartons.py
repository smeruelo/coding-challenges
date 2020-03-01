#!/usr/bin/python3
# https://www.codechef.com/WICP1901/problems/REACAR


def inversions(nums):
    count = 0

    def mergesort(array):

        def merge(left, right):
            nonlocal count
            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    count += len(left) - i
            if i >= len(left):
                merged.extend(right[j:])
            if j >= len(right):
                merged.extend(left[i:])

            return merged

        n = len(array)
        if n == 1:
            return array
        return merge(mergesort(array[:n//2]), mergesort(array[n//2:]))

    mergesort(nums)
    return count


input()
unordered = map(int, input().split())
ordered = map(int, input().split())
index = {k: v for v, k in enumerate(unordered)}
print(inversions(list(map(lambda x: index[x], ordered))))
