package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type dot struct {
	x int
	y int
}

type instruction struct {
	axis  string
	value int
}

func readInput(filename string) ([]dot, []instruction, dot) {
	dots := []dot{}
	instructions := []instruction{}
	maxDot := dot{x: 0, y: 0}

	data, _ := ioutil.ReadFile(filename)
	fileParts := strings.Split(string(data), "\n\n")

	for _, dotLine := range strings.Split(fileParts[0], "\n") {
		coordinate := strings.Split(dotLine, ",")
		x, _ := strconv.Atoi(coordinate[0])
		y, _ := strconv.Atoi(coordinate[1])
		dots = append(dots, dot{x: x, y: y})
		if x > maxDot.x {
			maxDot.x = x
		}
		if y > maxDot.y {
			maxDot.y = y
		}
	}

	for _, instrLine := range strings.Split(fileParts[1], "\n") {
		instr := strings.Split(instrLine, "=")
		axis := instr[0][len(instr[0])-1:]
		value, _ := strconv.Atoi(instr[1])
		instructions = append(instructions, instruction{axis: axis, value: value})
	}

	return dots, instructions, maxDot

}

func initPaper(dots []dot, maxDot dot) [][]bool {
	paper := make([][]bool, maxDot.y+1)
	for y := 0; y <= maxDot.y; y++ {
		paper[y] = make([]bool, maxDot.x+1)
	}

	for _, dot := range dots {
		paper[dot.y][dot.x] = true
	}

	return paper
}

func countDots(paper [][]bool) (count int) {
	for _, row := range paper {
		for _, col := range row {
			if col {
				count++
			}
		}
	}
	return count
}

func foldHorizontally(paper [][]bool, foldY int) [][]bool {
	for i := 1; i <= foldY; i++ {
		for x := 0; x < len(paper[foldY-i]); x++ {
			if foldY+i < len(paper) {
				paper[foldY-i][x] = paper[foldY-i][x] || paper[foldY+i][x]
			}
		}
	}
	return paper[:foldY]
}

func foldVertically(paper [][]bool, foldX int) [][]bool {
	for y := 0; y < len(paper); y++ {
		for i := 1; i <= foldX; i++ {
			paper[y][foldX-i] = paper[y][foldX-i] || paper[y][foldX+i]
		}
		paper[y] = paper[y][:foldX]
	}
	return paper
}

func printPaper(paper [][]bool) {
	for y := 0; y < len(paper); y++ {
		for x := 0; x < len(paper[y]); x++ {
			if paper[y][x] {
				fmt.Printf("# ")
			} else {
				fmt.Printf(". ")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func solvePart1(filename string) int {
	dots, instructions, maxDot := readInput(filename)
	paper := initPaper(dots, maxDot)
	var folded [][]bool

	switch instructions[0].axis {
	case "x":
		folded = foldVertically(paper, instructions[0].value)
	case "y":
		folded = foldHorizontally(paper, instructions[0].value)
	}
	return countDots(folded)
}

func solvePart2(filename string) {
	dots, instructions, maxDot := readInput(filename)
	paper := initPaper(dots, maxDot)

	for _, instr := range instructions {
		switch instr.axis {
		case "x":
			paper = foldVertically(paper, instr.value)
		case "y":
			paper = foldHorizontally(paper, instr.value)
		}
	}
	printPaper(paper)
}

func main() {
	fmt.Println("Part 1:", solvePart1("13_transparent_origami.input"))
	fmt.Println("Part 2:")
	solvePart2("13_transparent_origami.input")
}
