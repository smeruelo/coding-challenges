# Octal representation

A non-empty array A of N elements contains an octal representation of a non-negative integer K; i.e. each element of A lies within the range [0..7].
The integer K can be calculated using the following formula:

> K = A[0] * 8<sup>0</sup> + A[1] * 8<sup>1</sup> + ... + A[N-1] * 8<sup>N-1</sup>

Write a function ` def solution(A)` that returns the number of bits set to 1 in the binary representation of K.

For example, given the following array:

```
A[0] = 1
A[1] = 5
A[2] = 6
```
the value of K is 1 * 8<sup>0</sup> + 5 * 8<sup>1</sup> + 6 * 8<sup>2</sup> = 425.
Its binary representation is 110101001, which contains five bits set to 1, so the function should return 5.

Write an **efficient** algorithm for the following assumptions:

*   N is an integer within the range [1..100,000]
*   each element of array A is an integer within the range [0..7]
