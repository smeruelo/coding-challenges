package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func readInput(filename string) (string, map[string]string) {
	rules := map[string]string{}
	data, _ := ioutil.ReadFile(filename)
	fileParts := strings.Split(string(data), "\n\n")
	template := fileParts[0]
	for _, line := range strings.Split(fileParts[1], "\n") {
		ruleParts := strings.Split(line, " -> ")
		rules[ruleParts[0]] = ruleParts[1]
	}
	return template, rules
}

func initialPairs(template string, rules map[string]string) map[string]int {
	pairs := map[string]int{}
	for i := 0; i < len(template)-1; i++ {
		pairs[template[i:i+2]]++
	}
	return pairs
}

func nextStep(currentPairs map[string]int, rules map[string]string) map[string]int {
	nextPairs := map[string]int{}
	for k, v := range currentPairs {
		leftElement := string(k[0])
		rightElement := string(k[1])
		insertedElement := rules[k]
		nextPairs[leftElement+insertedElement] += v
		nextPairs[insertedElement+rightElement] += v
	}
	return nextPairs
}

func countElements(template string, pairs map[string]int) int {
	lastElement := template[len(template)-1]
	times := map[byte]int{}
	times[lastElement] = 1

	for k, v := range pairs {
		times[k[0]] += v
	}

	most := times[lastElement]
	least := times[lastElement]
	for _, v := range times {
		if v > most {
			most = v
		}
		if v < least {
			least = v
		}
	}

	return most - least
}

func polimer(template string, rules map[string]string, numSteps int) int {
	currentPairs := initialPairs(template, rules)
	for i := 0; i < numSteps; i++ {
		currentPairs = nextStep(currentPairs, rules)
	}
	return countElements(template, currentPairs)
}

func solvePart1(inputFile string) int {
	template, rules := readInput(inputFile)
	return polimer(template, rules, 10)
}

func solvePart2(inputFile string) int {
	template, rules := readInput(inputFile)
	return polimer(template, rules, 40)
}

func main() {
	fmt.Println("Part 1:", solvePart1("14_extended_polymerization.input"))
	fmt.Println("Part 2:", solvePart2("14_extended_polymerization.input"))
}
