// https://projecteuler.net/problem=1

package main

func is_multiple(i, j int) bool {
	return (i != 0) && ((i % j) == 0)
}

func sum(n int) int {
	acc := 0
	for i := 3; i < n; i++ {
		if is_multiple(i, 3) || is_multiple(i, 5) {
			acc += i
		}
	}
	return acc
}

func main() {
	print(sum(1000))
}
