// https://projecteuler.net/problem=3

package main

import "math"

func is_prime(n int) bool {
	i := int(math.Floor(math.Sqrt(float64(n))))
	prime := true
	for i > 1 && prime {
		if n%i == 0 {
			prime = false
		}
		i -= 1
	}
	return prime
}

func highest_factor(n int) int {
	i := int(math.Floor(math.Sqrt(float64(n))))
	factor := n
	for i > 1 && factor == n {
		if n%i == 0 && is_prime(i) {
			factor = i
		}
		i -= 1
	}
	return factor
}

func main() {
	print(highest_factor(600851475143))
}
