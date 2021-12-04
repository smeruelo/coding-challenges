package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func readFileIntoSlice(filename string) []string {
	data, _ := ioutil.ReadFile(filename)
	return strings.Split(string(data), "\n")
}

func gammaAndEpsilonRates(report []string) (int, int) {
	totalEntries := len(report)
	binaryLength := len(report[0])
	count := make([]int, binaryLength)

	for _, entry := range report {
		for i, bit := range entry {
			if bit == '1' {
				count[i]++
			}
		}
	}

	var zeros, gammaBit, epsilonBit, gammaRateDecimal, epsilonRateDecimal int
	for i, ones := range count {
		zeros = totalEntries - ones
		if ones >= zeros {
			gammaBit = 1
			epsilonBit = 0
		} else {
			gammaBit = 0
			epsilonBit = 1
		}
		gammaRateDecimal += int(math.Pow(2, float64(binaryLength-1-i))) * gammaBit
		epsilonRateDecimal += int(math.Pow(2, float64(binaryLength-1-i))) * epsilonBit
	}

	return gammaRateDecimal, epsilonRateDecimal
}

func runeToInt(r rune) int { return int(r - '0') }

func binaryStringToDecimal(s string) (d int) {
	maxPower := len(s) - 1
	for i, bit := range s {
		d += runeToInt(bit) * int(math.Pow(2, float64(maxPower-i)))
	}
	return d
}

func separateEntries(report []string, i int) (ones []string, zeros []string) {
	for _, entry := range report {
		if entry[i] == '1' {
			ones = append(ones, entry)
		} else {
			zeros = append(zeros, entry)
		}
	}
	return ones, zeros
}

func oxygenRate(report []string, i int) int {
	if len(report) == 1 {
		return binaryStringToDecimal(report[0])
	}

	ones, zeros := separateEntries(report, i)
	if len(ones) >= len(zeros) {
		return oxygenRate(ones, i+1)
	}
	return oxygenRate(zeros, i+1)
}

func co2Rate(report []string, i int) int {
	if len(report) == 1 {
		return binaryStringToDecimal(report[0])
	}

	ones, zeros := separateEntries(report, i)
	if len(ones) < len(zeros) {
		return co2Rate(ones, i+1)
	}
	return co2Rate(zeros, i+1)
}

func main() {
	report := readFileIntoSlice("03_binary_diagnostic.input")
	gammaRate, epsilonRate := gammaAndEpsilonRates(report)
	fmt.Println("Part 1:", gammaRate*epsilonRate)
	fmt.Println("Part 2:", oxygenRate(report, 0)*co2Rate(report, 0))
}
