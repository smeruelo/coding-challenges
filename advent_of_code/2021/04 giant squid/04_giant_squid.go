package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type cardboard [5][5]int
type cardboardLine [5]int

func stringToCardboardLine(s string) (line cardboardLine) {
	i := 0
	for _, token := range strings.Split(s, " ") {
		if token != "" {
			line[i], _ = strconv.Atoi(token)
			i++
		}
	}
	return line
}

func blockToCardboard(block string) (board cardboard) {
	for i, line := range strings.Split(block, "\n") {
		board[i] = stringToCardboardLine(line)
	}
	return board
}

func stringToNumbers(s string) (numbers []int) {
	var num_i int
	for _, num_s := range strings.Split(s, ",") {
		num_i, _ = strconv.Atoi(num_s)
		numbers = append(numbers, num_i)
	}
	return numbers
}

func readInput(filename string) ([]int, []cardboard) {
	data, _ := ioutil.ReadFile(filename)
	blocks := strings.Split(string(data), "\n\n")
	randomNumbers := stringToNumbers(blocks[0])

	allBoards := make([]cardboard, len(blocks)-1)
	for i, block := range blocks[1:] {
		allBoards[i] = blockToCardboard(block)
	}

	return randomNumbers, allBoards
}

func updateCardboard(board cardboard, ballNumber int) cardboard {
	for i, line := range board {
		for j, number := range line {
			if number == ballNumber {
				board[i][j] = -1
				return board
			}
		}
	}
	return board
}

func column(board cardboard, i int) (column cardboardLine) {
	for j := 0; j < 5; j++ {
		column[j] = board[j][i]
	}
	return column
}

func allMarked(line cardboardLine) bool {
	for i := 0; i < 5; i++ {
		if line[i] != -1 {
			return false
		}
	}
	return true

}

func sumUnmarked(board cardboard) (sum int) {
	for _, line := range board {
		for _, num := range line {
			if num > 0 {
				sum += num
			}
		}
	}
	return sum
}

func isWinner(board cardboard) bool {
	for _, row := range board {
		if allMarked(row) {
			return true
		}
	}
	for i := 0; i < 5; i++ {
		if allMarked(column(board, i)) {
			return true
		}
	}
	return false
}

func playBingoToWin(randomNumbers []int, allBoards []cardboard) (score int) {
	for _, num := range randomNumbers {
		for i := 0; i < len(allBoards); i++ {
			allBoards[i] = updateCardboard(allBoards[i], num)
			if isWinner(allBoards[i]) {
				return num * sumUnmarked(allBoards[i])
			}
		}
	}
	return (-1)
}

func playBingoToLose(randomNumbers []int, i int, allBoards []cardboard) (score int) {
	ballNumber := randomNumbers[i]
	loserBoards := make([]cardboard, 0, len(allBoards))

	for i := 0; i < len(allBoards); i++ {
		board := updateCardboard(allBoards[i], ballNumber)
		if isWinner(board) {
			if len(allBoards) == 1 {
				return ballNumber * sumUnmarked(board)
			}
		} else {
			loserBoards = append(loserBoards, board)
		}
	}
	return playBingoToLose(randomNumbers, i+1, loserBoards)
}

func main() {
	randomNumbers, boards := readInput("04_giant_squid.input")
	fmt.Printf("Part 1: %d\n", playBingoToWin(randomNumbers, boards))
	fmt.Printf("Part 2: %d\n", playBingoToLose(randomNumbers, 0, boards))
}
