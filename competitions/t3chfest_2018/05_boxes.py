#!/usr/bin/python3

def solution(A):
    if A == []:
        return 0

    # Two pointers method

    # Traverse the array from right to left to find the first element who breaks the sorting
    # That will be the right pointer
    end = len(A) - 1
    current = A[len(A) - 1]
    while end - 1 >= 0 and current >= A[end]:
        current = A[end]
        end -= 1
    if current < A[end]:
        end += 1
    if end == 0:
        return 0

    # Traverse from left to right and, for every position in the array,
    # (that will be the left pointer)
    # count how many elements would maintain the order if we removed all in between both pointers
    # Move the right pointer if needed
    begin = 0
    previous = -1
    maximum = boxes = len(A) - end
    print(A)
    print(begin, end, '-->', len(A) - boxes)
    while A[begin] >= previous:
        if end >= len(A) or A[begin] <= A[end]:
            previous = A[begin]
            begin += 1
            boxes += 1
        else:
            end += 1
            boxes -= 1
        maximum = max(maximum, boxes)
        print(begin, end, '-->', len(A) - boxes)
    return len(A) - maximum


if __name__ == '__main__':
    # Some tests
    print(solution([1, 2, 3, 1, 1, 5]), 2); print()
    print(solution([]), 0); print()
    print(solution([2, 1]), 1); print()
    print(solution([6, 1, 3, 8]), 1); print()
    print(solution([7, 10, 5, 6, 1]), 3); print()
    print(solution([2, 2, 9, 8, 3, 5, 9, 8, 10, 10, 10, 8, 3, 5, 5, 1, 6, 1, 7, 8]), 16); print()
    print(solution([3, 2, 5, 7]), 1); print()
    print(solution([2, 5, 7]), 0); print()
