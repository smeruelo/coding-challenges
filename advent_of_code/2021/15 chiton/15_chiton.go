package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type coordinate struct {
	y int
	x int
}

func readInput(filename string) [][]int {
	risks := [][]int{}
	data, _ := ioutil.ReadFile(filename)
	for _, line := range strings.Split(string(data), "\n") {
		row := []int{}
		for _, char := range line {
			n, _ := strconv.Atoi(string(char))
			row = append(row, n)
		}
		risks = append(risks, row)
	}
	return risks
}

func fullInput(risks [][]int) [][]int {
	size := len(risks)
	full := make([][]int, size*5)
	for y := 0; y < size; y++ {
		for j := 0; j < 5; j++ {
			full[size*j+y] = make([]int, size*5)
			for x := 0; x < size; x++ {
				for k := 0; k < 5; k++ {
					full[size*j+y][size*k+x] = wrap(risks[y][x] + j + k)
				}
			}
		}
	}
	return full
}

func wrap(n int) int {
	if n > 9 {
		return n%10 + 1
	}
	return n
}

func adjacents(point coordinate, size int) []coordinate {
	adj := []coordinate{}
	if point.y > 0 {
		adj = append(adj, coordinate{y: point.y - 1, x: point.x})
	}
	if point.y < size-1 {
		adj = append(adj, coordinate{y: point.y + 1, x: point.x})
	}
	if point.x > 0 {
		adj = append(adj, coordinate{y: point.y, x: point.x - 1})
	}
	if point.x < size-1 {
		adj = append(adj, coordinate{y: point.y, x: point.x + 1})
	}
	return adj
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func bestToVisit(toVisit map[coordinate]bool, path [][]int) coordinate {
	size := len(path)
	minimum := 10 * size * size
	var best coordinate
	for k, _ := range toVisit {
		if path[k.y][k.x] < minimum {
			minimum = path[k.y][k.x]
			best = k
		}
	}
	return best
}

func dijkstra(weights [][]int) int {
	size := len(weights)
	path := make([][]int, size)
	for y := 0; y < size; y++ {
		path[y] = make([]int, size)
		for x := 0; x < size; x++ {
			path[y][x] = 10 * size * size
		}
	}
	path[0][0] = 0

	visited := map[coordinate]bool{}
	toVisit := map[coordinate]bool{coordinate{y: 0, x: 0}: true}
	for len(toVisit) > 0 {
		current := bestToVisit(toVisit, path)
		delete(toVisit, current)
		for _, adj := range adjacents(current, size) {
			if !visited[adj] {
				tentative := path[current.y][current.x] + weights[adj.y][adj.x]
				path[adj.y][adj.x] = min(tentative, path[adj.y][adj.x])
				toVisit[coordinate{y: adj.y, x: adj.x}] = true
			}
		}
		visited[current] = true
	}
	return path[size-1][size-1]
}

func solvePart1(inputFile string) int {
	risks := readInput(inputFile)
	return dijkstra(risks)
}

func solvePart2(inputFile string) int {
	risks := fullInput(readInput(inputFile))
	return dijkstra(risks)
}

func main() {
	fmt.Println("Part 1:", solvePart1("15_chiton.input"))
	fmt.Println("Part 2:", solvePart2("15_chiton.input"))
}
