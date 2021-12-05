package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const diagramSize = 1000

type point struct {
	x int
	y int
}

type line struct {
	p1 point
	p2 point
}

type diagram [diagramSize][diagramSize]int

func parsePoint(s string) point {
	nums := strings.Split(s, ",")
	x, _ := strconv.Atoi(nums[0])
	y, _ := strconv.Atoi(nums[1])
	return point{x: x, y: y}
}

func readFileIntoSlice(filename string) []line {
	data, _ := ioutil.ReadFile(filename)
	fileLines := strings.Split(string(data), "\n")
	lines := make([]line, len(fileLines))

	for i, fileLine := range fileLines {
		points := strings.Split(fileLine, " -> ")
		p1 := parsePoint(points[0])
		p2 := parsePoint(points[1])
		lines[i] = line{p1, p2}
	}
	return lines
}

func numbersInBetween(n1, n2 int) (numbers []int) {
	for i := n1; i <= n2; i++ {
		numbers = append(numbers, i)
	}
	for i := n1; i >= n2; i-- {
		numbers = append(numbers, i)
	}

	return numbers
}

func pointsCoveredNoDiagonal(l line) (points []point) {
	if l.p1.x == l.p2.x {
		for _, y := range numbersInBetween(l.p1.y, l.p2.y) {
			points = append(points, point{x: l.p1.x, y: y})
		}
	}
	if l.p1.y == l.p2.y {
		for _, x := range numbersInBetween(l.p1.x, l.p2.x) {
			points = append(points, point{x: x, y: l.p1.y})
		}
	}
	return points
}

func pointsCovered(l line) (points []point) {
	if l.p1.x != l.p2.x && l.p1.y != l.p2.y {
		xs := numbersInBetween(l.p1.x, l.p2.x)
		ys := numbersInBetween(l.p1.y, l.p2.y)
		for i := 0; i < len(xs); i++ {
			points = append(points, point{x: xs[i], y: ys[i]})
		}
	} else {
		return pointsCoveredNoDiagonal(l)
	}
	return points
}

func ventLines(lines []line, coverFunc func(line) []point) diagram {
	var vl diagram
	for _, line := range lines {
		pc := coverFunc(line)
		for _, p := range pc {
			vl[p.y][p.x]++
		}
	}
	return vl
}

func countOverlaps(vl *diagram) int {
	count := 0
	for _, row := range vl {
		for _, col := range row {
			if col > 1 {
				count++
			}
		}
	}
	return count
}

func main() {
	lines := readFileIntoSlice("05_hydrothermal_venture.input")
	vl1 := ventLines(lines, pointsCoveredNoDiagonal)
	fmt.Printf("Part 1: %d\n", countOverlaps(&vl1))
	vl2 := ventLines(lines, pointsCovered)
	fmt.Printf("Part 2: %d\n", countOverlaps(&vl2))
}
