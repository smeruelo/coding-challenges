// https://exercism.io/my/solutions/c5526f43f30b49e28c14137271b2bbde

package prime

// isPrime determines whether a number is prime or not
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// Nth returns the n-th primer number
func Nth(nth int) (int, bool) {
	if nth < 1 {
		return 0, false
	}
	if nth == 1 {
		return 2, true
	}
	count := 1
	for n := 3; ; n += 2 {
		if isPrime(n) {
			count++
			if count == nth {
				return n, true
			}
		}
	}
}
