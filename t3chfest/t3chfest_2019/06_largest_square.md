# Largest square

A matrix A of size N*M containing boolean values is given. We say that a square of size L can be placed in A at position (X, Y) if:
* 0 < L ≤ min(N, M)
* 0 ≤ X ≤ N-L
* 0 ≤ Y ≤ M-L
* A[X+i][Y+j] = True for all 0 ≤ i ≤ L and 0 ≤ J < L

If a square of size L can be placed at (X, Y), and at (X+1, Y) or (X, Y+1), then we say that it can be moved (in a single move) from (X, Y) to, respectively, (X+1, Y) or (X, Y+1).

We are looking for the largest L such that:
* A square of size L can initially be placed at (0, 0)
* The square can be moved, by a sequence of moves, from (0, 0) to (N-L, M-L)

In other words, we are looking for the largest square that can be moved from the upper-left to the lower-right corner, over elements of the matrix that are equal to True, by moving it downwards and to the right.
In particular, if all elements of array A are True, then L = min(N, M).

Write a function `def solution(A)` that, given a matrix A of size N*M containing boolean values, returns size L of the largest square satisfying the above conditions.
If there is no such L, the function should return 0.

For example, given array A:
```
A[0][0] = True   A[0][1] = True   A[0][2] = True   A[0][3] = False
A[1][0] = True   A[1][1] = True   A[1][2] = True   A[1][3] = False
A[2][0] = True   A[2][1] = True   A[2][2] = True   A[2][3] = False
A[3][0] = True   A[3][1] = True   A[3][2] = True   A[3][3] = True
A[4][0] = False  A[4][1] = True   A[4][2] = True   A[4][3] = True
A[5][0] = True   A[5][1] = False  A[5][2] = True   A[5][3] = True
```
the function should return 2.

Given array A:
```
A[0][0] = True   A[0][1] = True   A[0][2] = False  A[0][3] = False
A[1][0] = True   A[1][1] = False  A[1][2] = False  A[1][3] = False
A[2][0] = False  A[2][1] = True   A[2][2] = False  A[2][3] = True
```
the function should return 0.

Given array A:
```
A[0][0] = True 
```
the function should return 1.

Write an **efficient** algorithm for the following assumptions:
* N and M are integers within the range [0..300]
