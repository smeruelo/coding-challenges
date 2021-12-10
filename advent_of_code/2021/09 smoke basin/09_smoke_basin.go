package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

const inputSize = 100

type coordinate struct {
	y int
	x int
}

func readInput(filename string) [inputSize][inputSize]int {
	heightmap := [inputSize][inputSize]int{}
	data, _ := ioutil.ReadFile(filename)
	for row, line := range strings.Split(string(data), "\n") {
		for col, char := range line {
			height, _ := strconv.Atoi(string(char))
			heightmap[row][col] = height
		}
	}
	return heightmap
}

func adjacents(point coordinate) []coordinate {
	adj := []coordinate{}
	if point.y > 0 {
		adj = append(adj, coordinate{y: point.y - 1, x: point.x})
	}
	if point.y < inputSize-1 {
		adj = append(adj, coordinate{y: point.y + 1, x: point.x})
	}
	if point.x > 0 {
		adj = append(adj, coordinate{y: point.y, x: point.x - 1})
	}
	if point.x < inputSize-1 {
		adj = append(adj, coordinate{y: point.y, x: point.x + 1})
	}
	return adj
}

func isLowPoint(point coordinate, heightmap [inputSize][inputSize]int) bool {
	for _, p := range adjacents(point) {
		if heightmap[p.y][p.x] <= heightmap[point.y][point.x] {
			return false
		}
	}
	return true
}

func riskLevel(heightmap [inputSize][inputSize]int) int {
	sum := 0
	for r, row := range heightmap {
		for c, col := range row {
			if isLowPoint(coordinate{y: r, x: c}, heightmap) {
				sum += 1 + col
			}
		}
	}
	return sum
}

func nexts(point coordinate,
	visited *[inputSize][inputSize]bool,
	heightmap [inputSize][inputSize]int,
) []coordinate {
	nextPoints := []coordinate{}
	for _, p := range adjacents(point) {
		if !visited[p.y][p.x] && heightmap[p.y][p.x] != 9 {
			nextPoints = append(nextPoints, coordinate{y: p.y, x: p.x})
		}
	}
	return nextPoints
}

func basin(
	toVisit []coordinate,
	visited *[inputSize][inputSize]bool,
	size int,
	heightmap [inputSize][inputSize]int,
) int {
	if len(toVisit) == 0 {
		return size
	}
	point := toVisit[0]
	if visited[point.y][point.x] {
		return basin(toVisit[1:], visited, size, heightmap)
	}

	visited[point.y][point.x] = true
	toVisit = append(toVisit, nexts(point, visited, heightmap)...)
	return basin(toVisit[1:], visited, size+1, heightmap)
}

func largestBasins(heightmap [inputSize][inputSize]int) []int {
	basinSizes := []int{}
	visited := [inputSize][inputSize]bool{}
	for r, row := range heightmap {
		for c := range row {
			point := coordinate{y: r, x: c}
			if isLowPoint(point, heightmap) {
				size := basin([]coordinate{point}, &visited, 0, heightmap)
				basinSizes = append(basinSizes, size)
			}
		}
	}
	sort.Ints(basinSizes)
	return basinSizes[len(basinSizes)-3:]
}

func main() {
	heightmap := readInput("09_smoke_basin.input")
	fmt.Printf("Part 1: %d\n", riskLevel(heightmap))

	largest := largestBasins(heightmap)
	fmt.Printf("Part 2: %d\n", largest[0]*largest[1]*largest[2])
}
