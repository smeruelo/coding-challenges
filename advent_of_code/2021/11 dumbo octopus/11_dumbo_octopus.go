package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const inputSize = 10

type coordinate struct {
	y int
	x int
}

func readInput(filename string) (energy [inputSize][inputSize]int) {
	data, _ := ioutil.ReadFile(filename)
	for row, line := range strings.Split(string(data), "\n") {
		for col, char := range line {
			n, _ := strconv.Atoi(string(char))
			energy[row][col] = n
		}
	}
	return energy
}

func adjacents(point coordinate) []coordinate {
	adj := []coordinate{}
	for y := point.y - 1; y <= point.y+1; y++ {
		for x := point.x - 1; x <= point.x+1; x++ {
			if y >= 0 && y < inputSize && x >= 0 && x < inputSize && !(y == point.y && x == point.x) {
				adj = append(adj, coordinate{y: y, x: x})
			}
		}
	}
	return adj
}

func incEnergy(energy *[inputSize][inputSize]int) {
	for row := 0; row < inputSize; row++ {
		for col := 0; col < inputSize; col++ {
			energy[row][col]++
		}
	}
}

func hasFlashed(octopus coordinate, flashed *map[int]bool) bool {
	_, ok := map[int]bool(*flashed)[10*octopus.y+octopus.x]
	return ok
}

func markFlashed(octopus coordinate, flashed *map[int]bool) {
	map[int]bool(*flashed)[10*octopus.y+octopus.x] = true
}

func resetEnergy(energy *[inputSize][inputSize]int, flashed *map[int]bool) {
	for k, _ := range *flashed {
		y := k / 10
		x := k % 10
		energy[y][x] = 0
	}
}

func initialFlashers(energy *[inputSize][inputSize]int) []coordinate {
	flashers := []coordinate{}
	for row := 0; row < inputSize; row++ {
		for col := 0; col < inputSize; col++ {
			if energy[row][col] > 9 {
				flashers = append(flashers, coordinate{y: row, x: col})
			}
		}
	}
	return flashers
}

func cascadeFlash(energy *[inputSize][inputSize]int, toExplore []coordinate, flashed *map[int]bool) {
	if len(toExplore) == 0 {
		return
	}

	current := toExplore[0]
	if hasFlashed(current, flashed) {
		cascadeFlash(energy, toExplore[1:], flashed)
		return
	}

	markFlashed(current, flashed)
	newFlashers := []coordinate{}
	for _, adj := range adjacents(current) {
		energy[adj.y][adj.x]++
		if energy[adj.y][adj.x] > 9 {
			newFlashers = append(newFlashers, adj)
		}
	}
	cascadeFlash(energy, append(toExplore[1:], newFlashers...), flashed)
}

func runStep(energy *[inputSize][inputSize]int) int {
	incEnergy(energy)

	toExplore := initialFlashers(energy)
	flashed := map[int]bool{}
	cascadeFlash(energy, toExplore, &flashed)

	resetEnergy(energy, &flashed)
	return len(flashed)
}

func solvePart1(inputFile string) int {
	energy := readInput(inputFile)
	count := 0
	for step := 0; step < 100; step++ {
		count += runStep(&energy)
	}
	return count
}

func solvePart2(inputFile string) int {
	energy := readInput(inputFile)
	step := 0
	for flashers := 0; flashers < inputSize*inputSize; step++ {
		flashers = runStep(&energy)
	}
	return step
}

func main() {
	fmt.Println("Part 1:", solvePart1("11_dumbo_octopus.input"))
	fmt.Println("Part 2:", solvePart2("11_dumbo_octopus.input"))
}
