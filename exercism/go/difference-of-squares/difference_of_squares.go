// https://exercism.io/my/solutions/d06121fc761d49e9bd08c16a820b94e1

package diffsquares

// SquareOfSum returns the square of the sum of the first n natural numbers.
func SquareOfSum(n int) int {
	sum := n * (n + 1) / 2
	return sum * sum
}

// SumOfSquares returns the sum of the squared first n natural numbers.
func SumOfSquares(n int) int {
	return n * (n + 1) * (2*n + 1) / 6
}

// Difference returns the square of the sum of the first n natural numbers
// minus the sum of the squared first n natural numbers.
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
