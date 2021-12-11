package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func readInput(filename string) []string {
	data, _ := ioutil.ReadFile(filename)
	return strings.Split(string(data), "\n")
}

var seScores = map[byte]int{')': 3, ']': 57, '}': 1197, '>': 25137}
var acScores = map[byte]int{'(': 1, '[': 2, '{': 3, '<': 4}
var openMatch = map[byte]byte{')': '(', ']': '[', '}': '{', '>': '<'}

func isCloseChar(char byte) bool {
	_, ok := openMatch[char]
	return ok
}

func pop(s *[]byte) byte {
	popped := []byte(*s)[len(*s)-1]
	*s = []byte(*s)[:len(*s)-1]
	return popped
}

func push(s *[]byte, char byte) {
	*s = append(*s, char)
}

func findChunkError(s string, stack *[]byte) *byte {
	if len(s) == 0 {
		return nil
	}

	char := s[0]

	if !isCloseChar(char) {
		push(stack, char)
		return findChunkError(s[1:], stack)
	}

	if len(*stack) > 0 {
		popped := pop(stack)
		if popped == openMatch[char] {
			return findChunkError(s[1:], stack)
		}
	}
	return &char
}

func syntaxErrorScore(subsystem []string) (score int) {
	for _, line := range subsystem {
		stack := []byte{}
		if err := findChunkError(line, &stack); err != nil {
			score += seScores[*err]
		}
	}
	return score
}

func solvePart1(inputFile string) int {
	subsystem := readInput(inputFile)
	return syntaxErrorScore(subsystem)
}

func autocompleteScore(subsystem []string) int {
	scores := []int{}
	for _, line := range subsystem {
		stack := []byte{}
		if findChunkError(line, &stack) == nil {
			lineScore := 0
			for len(stack) > 0 {
				popped := pop(&stack)
				lineScore = lineScore*5 + acScores[popped]
			}
			scores = append(scores, lineScore)
		}
	}
	sort.Ints(scores)
	return scores[len(scores)/2]
}

func solvePart2(inputFile string) int {
	subsystem := readInput(inputFile)
	return autocompleteScore(subsystem)
}

func main() {
	fmt.Printf("Part 1: %d\n", solvePart1("10_syntax_scoring.input"))
	fmt.Printf("Part 2: %d\n", solvePart2("10_syntax_scoring.input"))
}
