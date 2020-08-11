package matrix

import (
	"fmt"
	"strconv"
	"strings"
)

type matrix [][]int

func (m matrix) height() int {
	return len(m)
}

func (m matrix) width() int {
	if m.height() > 0 {
		return len(m[0])
	}
	return -1
}

func New(s string) (matrix, error) {
	m := matrix{}
	for i, line := range strings.Split(s, "\n") {
		rowS := strings.Fields(line)
		length := len(rowS)
		if i > 0 && length != m.width() {
			fmt.Println(rowS, length, m.width())
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
		m = append(m, rowI)
	}
	return m, nil
}

func (m *matrix) Set(row, col, val int) bool {
	if row >= 0 && row < m.height() && col >= 0 && col < m.width() {
		(*m)[row][col] = val
		return true
	}
	return false
}

func deepCopy(m matrix) matrix {
	copiedMatrix := make(matrix, m.height())
	for i, row := range m {
		copiedRow := make([]int, len(row))
		copy(copiedRow, row)
		copiedMatrix[i] = copiedRow
	}
	return copiedMatrix
}

func transpose(m matrix) matrix {
	transMatrix := make(matrix, m.width())
	for c := 0; c < m.width(); c++ {
		transRow := make([]int, m.height())
		for r := 0; r < m.height(); r++ {
			transRow[r] = m[r][c]
		}
		transMatrix[c] = transRow
	}
	return transMatrix
}

func (m matrix) Rows() [][]int {
	return [][]int(deepCopy(m))
}

func (m matrix) Cols() [][]int {
	return [][]int(transpose(m))
}
