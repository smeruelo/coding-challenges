// https://exercism.io/my/solutions/0e464bb92c684c829edf73bc79a51058

package matrix

import (
	"fmt"
	"strconv"
	"strings"
)

// Matrix type represents a two-dimensional slice of integers
type Matrix [][]int

func (m Matrix) height() int {
	return len(m)
}

func (m Matrix) width() int {
	if m.height() > 0 {
		return len(m[0])
	}
	return -1
}

// New creates a Matrix from a string
func New(s string) (Matrix, error) {
	lines := strings.Split(s, "\n")
	m := make(Matrix, len(lines))
	for i, line := range lines {
		rowS := strings.Fields(line)
		length := len(rowS)
		if i > 0 && length != m.width() {
			return m, fmt.Errorf("invalid input %q (all rows must have equal size)", s)
		}
		rowI := make([]int, length)
		for j := 0; j < length; j++ {
			n, err := strconv.Atoi(rowS[j])
			if err != nil {
				return m, fmt.Errorf("invalid input %q (elements must be integers)", s)
			}
			rowI[j] = n
		}
		m[i] = rowI
	}
	return m, nil
}

// Set sets the value of an specific element of a Matrix (in-place)
func (m Matrix) Set(row, col, val int) bool {
	if row >= 0 && row < m.height() && col >= 0 && col < m.width() {
		m[row][col] = val
		return true
	}
	return false
}

// Rows returns a slice of a Matrix's rows
func (m Matrix) Rows() [][]int {
	copiedArray := make([][]int, m.height())
	for i, row := range m {
		copiedRow := make([]int, len(row))
		copy(copiedRow, row)
		copiedArray[i] = copiedRow
	}
	return copiedArray
}

// Cols returns a slice of a Matrix's cols
func (m Matrix) Cols() [][]int {
	transArray := make([][]int, m.width())
	for c := 0; c < m.width(); c++ {
		transRow := make([]int, m.height())
		for r := 0; r < m.height(); r++ {
			transRow[r] = m[r][c]
		}
		transArray[c] = transRow
	}
	return transArray
}
