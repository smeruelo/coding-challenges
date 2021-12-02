package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func readFileIntoSlice(filename string) (nums []int) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(data), "\n")
	nums = make([]int, len(lines))
	for i, line := range lines {
		n, _ := strconv.Atoi(line)
		nums[i] = n
	}
	return nums
}

func countIncreases(measurements []int) int {
	count := 0
	for i := 1; i < len(measurements); i++ {
		if measurements[i] > measurements[i-1] {
			count++
		}
	}
	return count
}

func group(measurements []int) (nums []int) {
	nums = make([]int, len(measurements)-2)
	for i := 0; i <= len(measurements)-3; i++ {
		nums[i] = measurements[i] + measurements[i+1] + measurements[i+2]
	}
	return nums
}

func main() {
	measurements := readFileIntoSlice("01_sonar_sweep.input")
	fmt.Println("Part 1:", countIncreases(measurements))
	fmt.Println("Part 2:", countIncreases(group(measurements)))
}
