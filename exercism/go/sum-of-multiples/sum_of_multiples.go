// https://exercism.io/my/solutions/6db367aef2cd49aebd983f04e23a7585

package summultiples

func isMultiple(a, b int) bool {
	if b == 0 {
		return false
	}
	return a%b == 0
}

func isMultipleOfAny(n int, divisors []int) bool {
	for _, d := range divisors {
		if isMultiple(n, d) {
			return true
		}
	}
	return false
}

// SumMultiples calculates the sum of numbers < limit that are multiples of any of given divisors
func SumMultiples(limit int, divisors ...int) int {
	sum := 0
	for i := 1; i < limit; i++ {
		if isMultipleOfAny(i, divisors) {
			sum += i
		}
	}
	return sum
}
