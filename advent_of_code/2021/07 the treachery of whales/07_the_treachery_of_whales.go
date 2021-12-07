package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strconv"
	"strings"
)

func readInput(filename string) []int {
	data, _ := ioutil.ReadFile(filename)
	var numbers []int
	for _, numS := range strings.Split(string(data), ",") {
		numI, _ := strconv.Atoi(numS)
		numbers = append(numbers, numI)
	}
	return numbers
}

func odd(n int) bool {
	return n%2 == 0
}

func intAbs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func median(numbers []int) int {
	sort.Ints(numbers)
	i := len(numbers)
	if odd(i) {
		return numbers[i/2]
	}
	return int(numbers[i/2]+numbers[i-1/2]) / 2
}

func sumOfFuelWithMedian(numbers []int, median int) (sum int) {
	for _, num := range numbers {
		sum += intAbs(num - median)
	}
	return sum
}

func average(numbers []int) (int, int) {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	trunc := int(float64(sum) / float64(len(numbers)))
	ceil := int(math.Ceil(float64(sum) / float64(len(numbers))))
	return trunc, ceil
}

func sumOfFuelWithAverage(numbers []int, average int) (sum int) {
	for _, num := range numbers {
		distance := intAbs(num - average)
		sum += distance * (distance + 1) / 2
	}
	return sum
}

func min(n1, n2 int) int {
	if n1 < n2 {
		return n1
	}
	return n2
}

func main() {
	positions := readInput("07_the_treachery_of_whales.input")
	fmt.Printf("Part 1: %d\n", sumOfFuelWithMedian(positions, median(positions)))

	average1, average2 := average(positions)
	sum1 := sumOfFuelWithAverage(positions, average1)
	sum2 := sumOfFuelWithAverage(positions, average2)
	fmt.Printf("Part 2: %d\n", min(sum1, sum2))
}
