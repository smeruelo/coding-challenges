package main

import (
	"fmt"
	"io/ioutil"
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

func simulateLanternfish(timers []int, days int) int {
	count := make([]int, 9)
	for _, timer := range timers {
		count[timer]++
	}

	for i := 0; i < days; i++ {
		spawners := count[0]
		for j := 0; j < 8; j++ {
			count[j] = count[j+1]
		}
		count[8] = spawners
		count[6] += spawners
	}

	sum := 0
	for _, c := range count {
		sum += c
	}
	return sum
}

func main() {
	timers := readInput("06_lanternfish.input")
	fmt.Printf("Part 1: %d\n", simulateLanternfish(timers, 80))
	fmt.Printf("Part 2: %d\n", simulateLanternfish(timers, 256))
}
