// https://projecteuler.net/problem=2

package main

func sum_even_fibonacci(n int) int {
	last1 := 1
	last2 := 1
	acc := 0
	current := last1 + last2
	for current < n {
		if current%2 == 0 {
			acc += current
		}
		last2 = last1
		last1 = current
		current = last1 + last2
	}
	return acc
}

func main() {
	print(sum_even_fibonacci(4000000))
}
